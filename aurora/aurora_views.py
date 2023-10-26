from django.shortcuts import render
from django.db.models import Max
from django.contrib.auth.decorators import login_required, permission_required 
from aurora.models import (
    SummaryUserMonthInfo,
    SummaryUserDailyInfo,
    SummaryUserPeriodInfo,
    SummaryContentDailyInfo,
    SummaryScanDailyInfo
)

@login_required(login_url='aurora:login')
def index(request):
    context = {"page_title": "Dashboard"}
    all_data = SummaryUserDailyInfo.objects.all().order_by('-summary_dt')
    all_content_data = SummaryContentDailyInfo.objects.all().order_by('-summary_dt')
    all_scan_data = SummaryScanDailyInfo.objects.all().order_by('-summary_dt')
    total_user_cnt = SummaryUserDailyInfo.objects.aggregate(latest_total_user=Max('total_user'))['latest_total_user']
    new_user_cnt = SummaryUserDailyInfo.objects.aggregate(latest_new_user=Max('new_user'))['latest_new_user']
    normal_user_cnt = total_user_cnt - new_user_cnt
    context = {"all_data": all_data,"all_content_data":all_content_data,"all_scan_data": all_scan_data,"total_user_cnt":total_user_cnt,"new_user_cnt":new_user_cnt,"normal_user_cnt":normal_user_cnt}

    print("total_user_cnt",total_user_cnt,"new_user_cnt",new_user_cnt,"normal_user_cnt",normal_user_cnt)
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