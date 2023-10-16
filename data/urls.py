from data import data_views
from django.urls import path

app_name = 'data'

urlpatterns = [
    path("svc-user-status-daily/", data_views.svc_user_status_daily, name="svc-user-status-daily"),
    path("svc-user-status-month/", data_views.svc_user_status_month, name="svc-user-status-month"),
    path("svc-activity-user/", data_views.svc_activity_user, name="svc-activity-user"),
    path("scan-status-daily/", data_views.scan_status_daily, name="scan-status-daily"),
    path("scan-status-month/", data_views.scan_status_month, name="scan-status-month"),
    path("scan-activity-status/", data_views.scan_activity_status, name="scan-activity-status"),
    path('download_summary_as_csv/', data_views.download_summary_as_csv, name='download_summary_as_csv'),
    #path("scan-status/", data_views.scan_status, name="scan-status"),
]
