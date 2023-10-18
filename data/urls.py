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
    path('download-summary-as-csv-user-daily/', data_views.download_summary_as_csv_user_daily, name='download-summary-as-csv-user-daily'),
    path('download-summary-as-csv-user-month/', data_views.download_summary_as_csv_user_month, name='download-summary-as-csv-user-month'),
    path('download-summary-as-csv-active-user/', data_views.download_summary_as_csv_active_user, name='download-summary-as-csv-active-user'),
    path('download-summary-as-csv-scan-daily/', data_views.download_summary_as_csv_scan_daily, name='download-summary-as-csv-scan-daily'),
    path('download-summary-as-csv-scan-month/', data_views.download_summary_as_csv_scan_month, name='download-summary-as-csv-scan-month'),
    path('download-summary-as-csv-active-scan/', data_views.download_summary_as_csv_active_scan, name='download-summary-as-csv-active-scan'),
    #path("scan-status/", data_views.scan_status, name="scan-status"),
]
