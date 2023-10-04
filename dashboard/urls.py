"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users.forms import EmailValidationOnForgotPassword
from django.contrib.auth import views as auth_views
from aurora import aurora_views
from users import users_views
from data import data_views
from operation import operation_views

urlpatterns = [

    path('', include('aurora.urls', namespace='aurora')),

    path('admin/', admin.site.urls),
    path('reset_password/', auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('change-password/',
    #     auth_views.PasswordChangeView.as_view(template_name='zenix/change-password.html',
    #                                           success_url='/users/'),
    #     name='change-password'
    # ),
    path('password/', users_views.change_password, name='change_password'),

    # data
    path('data/', include('data.urls', namespace='data')),

    # operation
    path("operation/", include('operation.urls', namespace='operation')),

]
if settings.DEBUG == True or settings.DEBUG == False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Dashboard"
admin.site.site_title = "Dashboard"
admin.site.index_title = "Dashboard"


'''
1- Submit email form                           PasswordResetView.as_view()
2- Email sent success Message                  PasswordResetDoneView.as_view()
3- Link to password Rest form in email         PasswordResetConfirmView.as_view()
4- Password successfully changed message       PasswordResetCompleteView.as_view()

'''