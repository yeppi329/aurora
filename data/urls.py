from data import data_views
from django.urls import path

app_name = 'data'

urlpatterns = [
    path('user-status/', data_views.user_status, name="user-status"),
]