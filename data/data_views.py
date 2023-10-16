from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from aurora.models import (
    SummaryUserMonthInfo,
    SummaryUserDailyInfo,
    SummaryUserPeriodInfo,
)
from aurora.models import (
    SummaryScanDailyInfo,
    SummaryScanMonthInfo,
    SummaryScanHourInfo,
)
from django.http import HttpResponse
import csv


@login_required(login_url="aurora:login")
def index(request):
    context = {"page_title": "이용자 현황"}
    return render(request, "aurora/pages/data/svc-user-status-daily.html", context)


@login_required(login_url="aurora:login")
def svc_user_status_daily(request):
    all_data = SummaryUserDailyInfo.objects.all().order_by('-summary_dt')
    
    # 페이지당 항목 수 설정
    items_per_page = 25
    paginator = Paginator(all_data, items_per_page)

    # 현재 페이지 번호 가져오기
    page_number = request.GET.get('page')

    # 현재 페이지의 항목 가져오기
    page = paginator.get_page(page_number)

    context = {
        "page_title": "이용자 현황(일별)",
        "all_data": page,
    }
    return render(request, 'aurora/pages/data/svc-user-status-daily.html', context)


@login_required(login_url="aurora:login")
def svc_user_status_month(request):
    all_data = SummaryUserMonthInfo.objects.all().order_by('-summary_dt')
    
    
    # 페이지당 항목 수 설정
    items_per_page = 25
    paginator = Paginator(all_data, items_per_page)

    # 현재 페이지 번호 가져오기
    page_number = request.GET.get('page')

    # 현재 페이지의 항목 가져오기
    page = paginator.get_page(page_number)

    context = {
        "page_title": "이용자 현황(월별)",
        "all_data": page,
    }
    
    return render(request, 'aurora/pages/data/svc-user-status-month.html', context)

def download_summary_as_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="summary_user_month_info.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    header = [
        'Summary ID', '통계일자', '총 이용자 수', '신규 가입 이용자 수', '중지된 이용자 수',
        '삭제된 이용자 수', '재가입 이용자 수', '비활성 이용자 수', 'DAU', '생성일시'
    ]
    writer.writerow(header)

    summaries = SummaryUserMonthInfo.objects.all()
    for summary in summaries:
        writer.writerow([
            summary.summary_id, summary.summary_dt, summary.total_user, summary.new_user,
            summary.suspended_user, summary.deleted_user, summary.return_user,
            summary.inactive_user, summary.dau, summary.created_at
        ])

    return response

@login_required(login_url="aurora:login")
def svc_activity_user(request):
    context = {"page_title": "기간별 이용자"}
    all_data = SummaryUserPeriodInfo.objects.all().order_by('-summary_dt')
    
    
    # 페이지당 항목 수 설정
    items_per_page = 25
    paginator = Paginator(all_data, items_per_page)

    # 현재 페이지 번호 가져오기
    page_number = request.GET.get('page')

    # 현재 페이지의 항목 가져오기
    page = paginator.get_page(page_number)

    context = {
        "page_title": "기간별 이용자",
        "all_data": page,
    }

    return render(request, 'aurora/pages/data/svc-activity-user.html', context)

    context = {"page_title": "기간별 이용자", "all_data": all_data}
    return render(request, "aurora/pages/data/svc-activity-user.html", context)


@login_required(login_url="aurora:login")
def scan_status_daily(request):
    context = {"page_title": "스캔 현황(일별)"}
    
    # 데이터 조회
    all_data = SummaryScanDailyInfo.objects.all().order_by('-summary_dt')

    # 페이지당 항목 수 설정
    items_per_page = 25
    paginator = Paginator(all_data, items_per_page)

    # 현재 페이지 번호 가져오기
    page_number = request.GET.get('page')

    # 현재 페이지의 항목 가져오기
    page = paginator.get_page(page_number)

    context = {
        "page_title": "스캔 현황(일별)",
        "all_data": page,
    }
    return render(request, 'aurora/pages/data/scan-status-daily.html', context)


@login_required(login_url='aurora:login')
def scan_status_month(request):
    context = {"page_title": "스캔 현황(월별)"}

    all_data = SummaryScanMonthInfo.objects.all().order_by('-summary_dt')
    
    # 페이지당 항목 수 설정
    items_per_page = 25
    paginator = Paginator(all_data, items_per_page)

    # 현재 페이지 번호 가져오기
    page_number = request.GET.get('page')

    # 현재 페이지의 항목 가져오기
    page = paginator.get_page(page_number)

    context = {
        "page_title": "스캔 현황(월별)",
        "all_data": page,
    }
    return render(request, 'aurora/pages/data/scan-status-month.html', context)


@login_required(login_url="aurora:login")
def scan_activity_status(request):
    context = {"page_title": "스캔 현황(시간별)"}
    all_data = SummaryScanHourInfo.objects.all().order_by('-summary_dt','-summary_hour')
    
    # 페이지당 항목 수 설정
    items_per_page = 25
    paginator = Paginator(all_data, items_per_page)

    # 현재 페이지 번호 가져오기
    page_number = request.GET.get('page')

    # 현재 페이지의 항목 가져오기
    page = paginator.get_page(page_number)

    context = {
        "page_title": "스캔 현황(시간별)",
        "all_data": page,
    }
    return render(request, 'aurora/pages/data/scan-activity-status.html', context)
