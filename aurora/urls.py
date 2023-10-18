from django.urls import path
from aurora import aurora_views
from users import users_views

app_name = "aurora"

urlpatterns = [
    path("", aurora_views.index, name="index"),
    path("index/", aurora_views.index, name="index"),
    path("page-login/", aurora_views.page_login, name="page-login"),
    path("page-register/", aurora_views.page_register, name="page-register"),
    path(
        "page-forgot-password/",
        aurora_views.page_forgot_password,
        name="page-forgot-password",
    ),
    path("page-lock-screen/", aurora_views.page_lock_screen, name="page-lock-screen"),
    path("page-error-400/", aurora_views.page_error_400, name="page-error-400"),
    path("page-error-403/", aurora_views.page_error_403, name="page-error-403"),
    path("page-error-404/", aurora_views.page_error_404, name="page-error-404"),
    path("page-error-500/", aurora_views.page_error_500, name="page-error-500"),
    path("page-error-503/", aurora_views.page_error_503, name="page-error-503"),
    path("", aurora_views.index, name="index"),
    path("index/", aurora_views.index, name="index"),
    path("login/", users_views.login_user, name="login"),
    path("logout/", users_views.logout_user, name="logout"),
    path("signup/", users_views.signup, name="signup"),
    path("activate/<uidb64>/<token>/", users_views.activate, name="activate"),
    path("users/", users_views.users, name="users"),
    path("user-details/<int:id>/", users_views.user_details, name="user-details"),
    path("add-user/", users_views.add_user, name="add-user"),
    path("edit-user/<int:id>/", users_views.edit_user, name="edit-user"),
    path("delete-user/<int:id>/", users_views.delete_user, name="delete-user"),
    path("permissions/", users_views.permissions, name="permissions"),
    path(
        "edit-permissions/<int:id>/",
        users_views.edit_permissions,
        name="edit-permissions",
    ),
    path(
        "delete-permissions/<int:id>/",
        users_views.delete_permissions,
        name="delete-permissions",
    ),
    path(
        "assign-permissions-to-user/<int:id>/",
        users_views.assign_permissions_to_user,
        name="assign-permissions-to-user",
    ),
]
