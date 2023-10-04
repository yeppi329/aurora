from data import data_views
from django.urls import path

app_name = 'data'

urlpatterns = [
    path("svc-user-status/", data_views.svc_user_status, name="svc-user-status"),
    path("scan-status/", data_views.scan_status, name="scan-status"),
]