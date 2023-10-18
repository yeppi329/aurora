from users import users_views
from django.urls import path, re_path

app_name = "users"

urlpatterns = [

    # Roles(Groups)
    path("authority/roles/", users_views.role_list, name="roles"),
    path("authority/roles/<int:id>", users_views.role_user_list, name="role-users"),

    # Permissions
    path("authority/permission/", users_views.permission_list, name="permission-list"),

]

