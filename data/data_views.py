from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='aurora:login')
def index(request):
    context = {"page_title": "이용자 현황"}
    return render(request, 'aurora/pages/data/svc-user-status.html', context)

@login_required(login_url='aurora:login')
def svc_user_status(request):
    context = {"page_title": "이용자 현황"}
    return render(request, 'aurora/pages/data/svc-user-status.html', context)

@login_required(login_url='aurora:login')
def scan_status(request):
    context = {"page_title": "스캔 현황"}
    return render(request, 'aurora/pages/data/scan-status.html', context)

