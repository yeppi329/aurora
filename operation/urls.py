from operation import operation_views
from django.urls import path

app_name = 'operation'

urlpatterns = [
    path("svc-user-list/", operation_views.svc_user_list, name="svc-user-list"),
    path("object-list/", operation_views.object_list, name="object-list"),
    path("content-list/", operation_views.content_list, name="content-list"),
    path("report-list/", operation_views.report_list, name="report-list"),
]
