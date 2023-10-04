from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='aurora:login')
def index(request):
    context = {"page_title": "이용자 관리"}
    return render(request, 'aurora/pages/operation/svc-user-list.html', context)

@login_required(login_url='aurora:login')
def svc_user_list(request):
    context = {"page_title": "이용자 관리"}
    return render(request, 'aurora/pages/operation/svc-user-list.html', context)

@login_required(login_url='aurora:login')
def object_list(request):
    context = {"page_title": "사물 관리"}
    return render(request, 'aurora/pages/operation/object-list.html', context)

@login_required(login_url='aurora:login')
def content_list(request):
    context = {"page_title": "이용자 관리"}
    return render(request, 'aurora/pages/operation/content-list.html', context)

@login_required(login_url='aurora:login')
def report_list(request):
    context = {"page_title": "사물 관리"}
    return render(request, 'aurora/pages/operation/report-list.html', context)

# Create your views here.
