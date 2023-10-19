from django.contrib.postgres.aggregates import StringAgg
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.db.models import F, CharField, Subquery, Value
from django.db.models.functions import Concat
from users.models import NewUser, GroupExpended
from users.forms import (
    NewUserForm,
    SignupForm,
    LoginForm,
    RoleForm,
    PermissionsForm,
    UserPermissionsForm,
    EditUserForm,
)
from aurora.models import Category
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, Permission
from django.db.models import Subquery, OuterRef, Count
from django.http import HttpResponse, JsonResponse
from django.contrib.contenttypes.models import ContentType

from django.core.paginator import Paginator

from django.conf import settings
from users.tokens import account_activation_token
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect


@login_required(login_url="aurora:login")
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Update Successfully")
            return redirect("/password/")
        else:
            messages.warning(request, "Form is not valid")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "aurora/modules/change-password.html", {"form": form})


@login_required(login_url="aurora:login")
@permission_required({"users.view_newuser"}, raise_exception=True)
def users(request):
    user_list = NewUser.objects.order_by("groups__name")
    total_user_count = NewUser.objects.order_by("groups__name").count()
    context = {"user_list": user_list, "total_user_count": total_user_count}
    return render(request, "aurora/modules/users.html", context)


@login_required(login_url="aurora:login")
@permission_required({"users.view_newuser"}, raise_exception=True)
def user_details(request, id):
    user_obj = get_object_or_404(NewUser, id=id)

    context = {
        "user_obj": user_obj,
        "user_group_perms": user_obj.get_group_permissions(),
        "user_perms": user_obj.get_user_permissions(),
    }

    return render(request, "aurora/modules/user-details.html", context)


@login_required(login_url="aurora:login")
@permission_required(
    {"users.view_newuser", "users.delete_newuser"}, raise_exception=True
)
def delete_user(request, id):
    u = NewUser.objects.get(id=id)
    u.delete()
    messages.success(request, "User deleted successfully")
    return redirect("aurora:users")


@login_required(login_url="aurora:login")
@permission_required({"users.view_newuser", "users.add_newuser"}, raise_exception=True)
def add_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save()
            user_obj.groups.clear()
            for i in form.cleaned_data.get("groups"):
                user_obj.groups.add(i)
            messages.success(
                request,
                f"{user_obj.first_name} {user_obj.last_name} is created successfully",
            )
            return redirect("aurora:users")
    else:
        form = NewUserForm()
    return render(request, "aurora/modules/add-user.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.is_active = False
            user_obj.save()
            # Default Group assign Start -------------------------------------------------------
            if Group.objects.filter(name="Customer"):
                user_obj.groups.add(Group.objects.filter(name="Customer")[0])
            else:
                Customer_group, created = Group.objects.get_or_create(name="Customer")
                content_type = ContentType.objects.get_for_model(NewUser)
                NewUser_permission = Permission.objects.filter(
                    content_type=content_type
                )
                for perm in NewUser_permission:
                    if perm.codename == "view_newuser":
                        Customer_group.permissions.add(perm)
                user_obj.groups.add(Customer_group)
            # Default Group assign End-----------------------------------------------------------
            try:
                if user_obj.is_active == False:
                    messages.warning(
                        request,
                        "Please confirm your email address to complete the registration.",
                    )
                return redirect("aurora:login")
            except:
                messages.warning(request, "Email Not valid")
                user_obj.delete()
        else:
            messages.warning(request, "Form is not valid")
    else:
        if request.user.is_authenticated:
            return redirect("aurora:index")
        form = SignupForm()
    return render(request, "aurora/modules/signup.html", {"form": form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = NewUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, NewUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("aurora:index")
    else:
        # return render(request, 'aurora/modules/account_activation/account_activation_invalid.html')
        return HttpResponse("Invalid")


@login_required(login_url="aurora:login")
@permission_required(
    {"users.view_newuser", "users.change_newuser"}, raise_exception=True
)
def edit_user(request, id):
    user_obj = get_object_or_404(NewUser, id=id)
    if request.method == "POST":
        form = EditUserForm(request.POST, request.FILES, instance=user_obj)
        if form.is_valid():
            user_obj = form.save()
            user_obj.groups.clear()
            for i in form.cleaned_data["groups"]:
                user_obj.groups.add(i)
            return redirect("aurora:users")
    else:
        form = EditUserForm(instance=user_obj)
    return render(request, "aurora/modules/add-user.html", {"form": form})


def login_user(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user is not None and user.is_active:
                login(request, user)
                usergroup = ",".join(request.user.groups.values_list("name", flat=True))
                messages.success(request, f"Welcome To {usergroup} Dashborad")
                next_url = request.GET.get("next")
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return redirect("aurora:index")
            else:
                messages.warning(request, "User is Not Active")

        else:
            messages.warning(
                request, "Form is Not valid! Please Check The Email and Password"
            )
            return render(request, "aurora/modules/login.html", context={"form": form})
    else:
        if request.user.is_authenticated:
            return redirect("aurora:index")
        form = LoginForm()
    return render(request, "aurora/modules/login.html", context={"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect("aurora:login")


@login_required(login_url="aurora:login")
@permission_required({"auth.view_group"}, raise_exception=True)
def groups_list(request):
    context = {
        "groups": Group.objects.annotate(
            user_count=Count("newuser", distinct=True)
        ).annotate(perms_count=Count("permissions", distinct=True)),
        "colors": {"primary": "primary", "success": "success", "dark": "dark"},
    }
    return render(request, "aurora/modules/group-list.html", context)


# 권한 관리 > 롤 관리
@login_required(login_url="aurora:login")
@permission_required({"auth.view_group"}, raise_exception=True)
def role_list(request):
    context = {
        "total": len(NewUser.objects.all()),
        "roles": Group.objects.annotate(
            user_count=Count("newuser", distinct=True)
        ).annotate(perms_count=Count("permissions", distinct=True)),
        "colors": {"primary": "primary", "success": "success", "dark": "dark"},
    }
    return render(request, "aurora/modules/role-list.html", context)


# 권한 관리 > 롤 관리 > 롤 추가
@login_required(login_url="aurora:login")
@permission_required({"auth.view_group", "auth.add_group"}, raise_exception=True)
def role_add(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            group = Group.objects.create(name=form.cleaned_data["name"])
            group_expended = GroupExpended.objects.create(group=group, description=form.cleaned_data["description"])
            group_expended.save()

            messages.success(request, "Group Created Successfully")
            return redirect("users:roles")
        else:
            messages.warning(request, "Name Already Exist")
            return render(request, "aurora/modules/role-add.html", {"form": form})
    else:
        form = RoleForm()
        return render(request, "aurora/modules/role-add.html", {"form": form})

# 권한 관리 > 롤 관리 > 롤 수정
@login_required(login_url="aurora:login")
@permission_required({"auth.view_group", "auth.change_group"}, raise_exception=True)
def role_edit(request, id):
    group_obj = Group.objects.filter(id=id).first()
    group_obj_expended = GroupExpended.objects.filter(group_id=group_obj.id).get()
    group_obj_expended.group = group_obj

    if request.method == "POST":
        data = dict(request.POST)
        try:
            if "permissions[]" in data:
                group_obj.permissions.clear()
                group_obj.permissions.set(data["permissions[]"])
            else:
                group_obj.permissions.clear()

            group_obj.name = data["name"][0]
            group_obj.save()

            group_obj_expended.group.name = group_obj
            group_obj_expended.group.permissions.set(data["permissions[]"])
            group_obj_expended.description = data["description"][0]
            group_obj_expended.save()

            response = JsonResponse({"success": "Save Successfully"})
            response.status_code = 200
            return response

        except:
            response = JsonResponse({"error": "Group Name already exist"})
            response.status_code = 403
            return response
    else:
        category_perm = Permission.objects.raw("""
        select * from (
            select t1.id, t1.codename, t2.order as order_clause, t2.category_desc, t2.uri,
                    (select concat('ALL, ', string_agg(x.category_desc::text, ', ')) from aurora_category x where x.parent_id = t2.category_id and x.parent_id != 0) as sub_category
            from auth_permission t1 inner join aurora_category t2 on t1.codename = t2.category_name
            where t2.parent_id = 0
        ) t order by order_clause
        """
        )

        perm_list = []
        for perm in category_perm:
            is_checked = False
            for group_perm in group_obj.permissions.all():
                if perm.id == group_perm.id:
                    is_checked = True
            perm_list.append({"id": perm.id, "name": perm.category_desc, "is_checked": is_checked})

        form = {
            "description": group_obj_expended.description,
            "name": group_obj.name,
            "group_id": group_obj.id,
            "permissions": perm_list,
        }

    return render(request, "aurora/modules/role-edit.html", {"form": form, })

# 권한 관리 > 롤 관리 > 롤 삭제
@login_required(login_url="aurora:login")
@permission_required({"auth.view_group", "auth.delete_group"}, raise_exception=True)
def role_delete(request, id):
    g = get_object_or_404(Group, id=id)

    g.delete()
    messages.success(request, "Group Deleted Sucessfully")

    return redirect("users:roles")


# 권한 관리 > 롤 관리 > 롤 사용자 리스트
@login_required(login_url="aurora:login")
@permission_required({"auth.view_group"}, raise_exception=True)
def role_user_list(request, id):
    user_list = NewUser.objects.filter(groups__id=id).all()
    paginator = Paginator(user_list, 20)

    context = {
        "total": Group.objects.annotate(user_count=Count("newuser", distinct=True)).filter(id=id).first().user_count,
        "role_info": Group.objects.get(id=id),
        "user_list": paginator.get_page(request.GET.get("page")),
        "colors": {"primary": "primary", "success": "success", "dark": "dark"},
    }
    return render(request, "aurora/modules/role-user-list.html", context)

# 권한 관리 > 허가 관리
@login_required(login_url="aurora:login")
@permission_required({"auth.view_permission"}, raise_exception=True)
def permission_list(request):

    raw_sql = """
select 0 as id, 0 as order_clause, 'ALL' as category_desc, 'All Category' as uri, 'ALL' as sub_category
union
select * from (
    select t1.id, t2.order as order_clause, t2.category_desc, t2.uri,
           (select concat('ALL, ', string_agg(x.category_desc::text, ', ')) from aurora_category x where x.parent_id = t2.category_id and x.parent_id != 0) as sub_category
    from auth_permission t1 inner join aurora_category t2 on t1.codename = t2.category_name
    where t2.parent_id = 0
) t order by order_clause
"""
    permission_menu_list = Permission.objects.raw(raw_sql)
    context = {
        "permissions_obj": permission_menu_list,
    }
    return render(request, "aurora/modules/permission-list.html", context)


# ======================================================================


@login_required(login_url="aurora:login")
@permission_required({"auth.view_permission"}, raise_exception=True)
def permissions(request):
    permission_list = Permission.objects.all()
    paginator = Paginator(permission_list, 10)  # Show 10 permission per page.
    context = {
        "permissions_obj": paginator.get_page(request.GET.get("page")),
    }

    return render(request, "aurora/modules/permissions.html", context)


@login_required(login_url="aurora:login")
@permission_required(
    {"auth.view_permission", "auth.change_permission"}, raise_exception=True
)
def edit_permissions(request, id):
    perm_obj = get_object_or_404(Permission, id=id)
    if request.method == "POST":
        form = PermissionsForm(request.POST, instance=perm_obj)

        if form.is_valid():
            form.save()
            return redirect("aurora:permissions")
    else:
        form = PermissionsForm(instance=perm_obj)
        return render(request, "aurora/modules/edit-permissions.html", {"form": form})


@login_required(login_url="aurora:login")
@permission_required(
    {"auth.view_permission", "auth.delete_permission"}, raise_exception=True
)
def delete_permissions(request, id):
    perm_obj = get_object_or_404(Permission, id=id)
    perm_obj.delete()
    messages.success(request, "Permission Delete Successfully")
    return redirect("aurora:permissions")


@login_required(login_url="aurora:login")
@permission_required(
    {"auth.view_permission", "auth.add_permission", "auth.change_permission"},
    raise_exception=True,
)
def assign_permissions_to_user(request, id):
    user_obj = get_object_or_404(NewUser, id=id)
    if request.method == "POST":
        queryDict = request.POST
        data = dict(queryDict)

        if "user_permissions[]" in data:
            user_obj.user_permissions.clear()
            user_obj.user_permissions.set(data["user_permissions[]"])
        else:
            user_obj.user_permissions.clear()
        response = JsonResponse({"success": "Save Successfully"})
        response.status_code = 200
        return response

    else:
        form = UserPermissionsForm(instance=user_obj)
    return render(
        request, "aurora/modules/assign_permissions_to_user.html", {"form": form}
    )
