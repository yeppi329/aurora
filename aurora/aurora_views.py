from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required 


@login_required(login_url='aurora:login')
def index(request):
    context = {"page_title": "Dashboard"}
    return render(request, 'aurora/index.html', context)

@login_required(login_url='aurora:login')
def page_login(request):
    return render(request, 'aurora/pages/page-login.html')


@login_required(login_url='aurora:login')
def page_register(request):
    return render(request, 'aurora/pages/page-register.html')


@login_required(login_url='aurora:login')
def page_lock_screen(request):
    return render(request, 'aurora/pages/page-lock-screen.html')


@login_required(login_url='aurora:login')
def page_forgot_password(request):
    return render(request, 'aurora/pages/page-forgot-password.html')


def page_error_400(request):
    return render(request, '400.html')


def page_error_403(request):
    return render(request, '403.html')


def page_error_404(request):
    return render(request, '404.html')


def page_error_500(request):
    return render(request, '500.html')


def page_error_503(request):
    return render(request, '503.html')