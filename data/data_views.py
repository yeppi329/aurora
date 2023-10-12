from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from aurora.models import SummaryUserMonthInfo, SummaryUserDailyInfo
from aurora.models import (
    SummaryScanDailyInfo,
    SummaryScanMonthInfo,
    SummaryScanHourInfo,
)


@login_required(login_url="aurora:login")
def index(request):
    context = {"page_title": "이용자 현황"}
    return render(request, "aurora/pages/data/svc-user-status-daily.html", context)


@login_required(login_url="aurora:login")
def svc_user_status_daily(request):
    all_data = SummaryUserDailyInfo.objects.all()
    for data in all_data:
        print(
            f"Summary ID: {data.summary_id}, Date: {data.summary_dt}, Total Users: {data.total_user}, deleted_user: {data.deleted_user}"
        )

    context = {"page_title": "이용자 현황(일별)", "all_data": all_data}
    return render(request, "aurora/pages/data/svc-user-status-daily.html", context)


@login_required(login_url="aurora:login")
def svc_user_status_month(request):
    all_data = SummaryUserMonthInfo.objects.all()
    for data in all_data:
        print(
            f"Summary ID: {data.summary_id}, Date: {data.summary_dt}, Total Users: {data.total_user}, deleted_user: {data.deleted_user}"
        )

    context = {"page_title": "이용자 현황(월별)", "all_data": all_data}
    return render(request, "aurora/pages/data/svc-user-status-month.html", context)


@login_required(login_url="aurora:login")
def svc_activity_user(request):
    context = {"page_title": "기간별 이용자"}
    all_data = SummaryUserPeriodInfo.objects.all()
    for data in all_data:
        print(
            f"Summary ID: {data.summary_id}, Date: {data.summary_dt}, use_day_7: {data.use_day_7}"
        )

    context = {"page_title": "기간별 이용자", "all_data": all_data}
    return render(request, "aurora/pages/data/svc-activity-user.html", context)


@login_required(login_url="aurora:login")
def scan_status_daily(request):
    context = {"page_title": "스캔 현황(일별)"}
    all_data = SummaryScanDailyInfo.objects.all()
    for data in all_data:
        print(
            f"Summary ID: {data.summary_id}, Date: {data.summary_dt}, scan_success: {data.scan_success}"
        )

    context = {"page_title": "스캔 현황(일별)", "all_data": all_data}
    return render(request, "aurora/pages/data/scan-status-daily.html", context)


@login_required(login_url="aurora:login")
def scan_status_month(request):
    context = {"page_title": "스캔 현황(월별)"}
    all_data = SummaryScanMonthInfo.objects.all()
    for data in all_data:
        print(
            f"Summary ID: {data.summary_id}, Date: {data.summary_dt}, scan_success: {data.scan_success}"
        )

    context = {"page_title": "스캔 현황(월별)", "all_data": all_data}
    return render(request, "aurora/pages/data/scan-status-month.html", context)


@login_required(login_url="aurora:login")
def scan_activity_status(request):
    context = {"page_title": "스캔 현황(시간별)"}
    all_data = SummaryScanHourInfo.objects.all()
    for data in all_data:
        print(
            f"Summary ID: {data.summary_id}, Date: {data.summary_dt}, scan_success: {data.scan_success}"
        )

    context = {"page_title": "스캔 현황(시간별)", "all_data": all_data}
    return render(request, "aurora/pages/data/scan-activity-status.html", context)
