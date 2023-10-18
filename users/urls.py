from users import users_views
from django.urls import path, re_path

app_name = "users"

urlpatterns = [

    # Roles(Groups)
    path("authority/roles/", users_views.role_list, name="roles"),
    path("authority/roles/<int:id>", users_views.role_user_list, name="role-users"),

    path("authority/roles/role/add", users_views.role_add, name="role-add"),
    path("authority/roles/role/edit/<int:id>", users_views.role_edit, name="role-edit"),
    path("authority/roles/role/delete/<int:id>", users_views.role_delete, name="role-delete"),

    # Permissions
    path("authority/permission/", users_views.permission_list, name="permission-list"),

]

