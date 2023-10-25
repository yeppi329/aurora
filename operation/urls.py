from operation import operation_views
from django.urls import path, re_path

app_name = "operation"

urlpatterns = [
    path("svc-user-list/", operation_views.svc_user_list, name="svc-user-list"),
    path("content-list/", operation_views.content_list, name="content-list"),
    path("report-list/", operation_views.report_list, name="report-list"),
    # 이용자 관리
    path("user-management/", operation_views.user_management, name="user-management"),
    re_path(
        r"^user-management/account-id-detail/(?P<account_id>[\w-]+)/$",
        operation_views.accountid_detail,
        name="user-management-account-id-detail",
    ),
    # 사물관리
    path("object-list/", operation_views.object_list, name="object-list"),
    re_path(
        r"^object-list/(?P<object_type>mg_id|scan_id|user_id)/$",
        operation_views.object_list,
        name="object-list-dynamic",
    ),
    re_path(
        r"^object-list/mg-id-detail/(?P<mg_id>[\w\W]+)/$",
        operation_views.mgid_detail,
        name="object-list-mg-id-detail",
    ),
    re_path(
        r"^object-list/scan-id-detail/(?P<scan_id>[\w-]+)/$",
        operation_views.scanid_detail,
        name="object-list-scan-id-detail",
    ),
    re_path(
        r"^object-list/user-id-detail/(?P<user_id>[\w-]+)/$",
        operation_views.userid_detail,
        name="object-list-user-id-detail",
    ),
    # new mg_id
    path("new-mg-id/", operation_views.new_mgid, name="new-mg-id"),
    re_path(
        r"^new-mg-id/(?P<scan_id>[\w\W]+)/$",
        operation_views.new_mgid_detail,
        name="new-mg-id-detail",
    ),
]
