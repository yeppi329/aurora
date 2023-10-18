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

def download_summary_as_csv_user_daily(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="SummaryUserDailyInfo.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    header = [
        '통계일자', '전체 회원 수','전체 회원 DAU' '신규 회원 수','신규 회원 DAU', '정지 회원',
        '탈퇴 회원', '복귀 회원', '휴면 회원'
    ]
    writer.writerow(header)

    summaries = SummaryUserDailyInfo.objects.all()
    for summary in summaries:
        writer.writerow([
            summary.summary_dt, summary.total_user,summary.dau, summary.new_user,summary.dau, 
            summary.suspended_user, summary.deleted_user, summary.return_user,
            summary.inactive_user
        ])

    return response

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

def download_summary_as_csv_user_month(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="SummaryUserMonthInfo.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    header = [
        '통계일자', '전체 회원 수','전체 회원 DAU' '신규 회원 수','신규 회원 DAU', '정지 회원',
        '탈퇴 회원', '복귀 회원', '휴면 회원'
    ]
    writer.writerow(header)

    summaries = SummaryUserMonthInfo.objects.all()
    for summary in summaries:
        writer.writerow([
            summary.summary_dt, summary.total_user,summary.dau, summary.new_user,summary.dau, 
            summary.suspended_user, summary.deleted_user, summary.return_user,
            summary.inactive_user
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

def download_summary_as_csv_active_user(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="SummaryUserPeriodInfo.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    header = [
        '통계일자', '07일 이용자', '30일 이용자', '60일 이용자',
        '90일 이용자'
    ]
    writer.writerow(header)

    summaries = SummaryUserPeriodInfo.objects.all()
    for summary in summaries:
        writer.writerow([
            summary.summary_dt, summary.use_day_7, summary.use_day_30,
            summary.use_day_60, summary.use_day_90
        ])

    return response

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

def download_summary_as_csv_scan_daily(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="SummaryScanDailyInfo.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    header = [
        '통계일자', '스캔_성공', '스캔_실패', '합계',
        '스캔 참여 회원 수', '인당 스캔 수', '스캔 비율_성공', '스캔 비율_실패', '평균 스캔 회원 수_성공', '평균 스캔 회원 수_실패'
    ]
    writer.writerow(header)

    summaries = SummaryScanDailyInfo.objects.all()
    for summary in summaries:
        writer.writerow([
            summary.summary_dt, summary.scan_success, summary.scan_fail,
            summary.scan_success + summary.scan_fail, summary.total_scan_user,
            (summary.scan_success + summary.scan_fail)/summary.total_scan_user if summary.total_scan_user > 0 else 0,
            summary.scan_success/(summary.scan_success + summary.scan_fail) * 100 if (summary.scan_success + summary.scan_fail) > 0 else 0,
            summary.scan_fail/(summary.scan_success + summary.scan_fail) * 100 if (summary.scan_success + summary.scan_fail) > 0 else 0,
            summary.scan_success/summary.total_scan_user if summary.total_scan_user > 0 else 0,
            summary.scan_fail/summary.total_scan_user if summary.total_scan_user > 0 else 0
            
        ])

    return response

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

def download_summary_as_csv_scan_month(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="SummaryScanMonthInfo.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    header = [
        '통계일자', '스캔_성공', '스캔_실패', '합계',
        '스캔 참여 회원 수', '인당 스캔 수', '스캔 비율_성공', '스캔 비율_실패', '평균 스캔 회원 수_성공', '평균 스캔 회원 수_실패'
    ]
    writer.writerow(header)

    summaries = SummaryScanMonthInfo.objects.all()
    for summary in summaries:
        writer.writerow([
            summary.summary_dt, summary.scan_success, summary.scan_fail,
            summary.scan_success + summary.scan_fail, summary.total_scan_user,
            (summary.scan_success + summary.scan_fail)/summary.total_scan_user if summary.total_scan_user > 0 else 0,
            summary.scan_success/(summary.scan_success + summary.scan_fail) * 100 if (summary.scan_success + summary.scan_fail) > 0 else 0,
            summary.scan_fail/(summary.scan_success + summary.scan_fail) * 100 if (summary.scan_success + summary.scan_fail) > 0 else 0,
            summary.scan_success/summary.total_scan_user if summary.total_scan_user > 0 else 0,
            summary.scan_fail/summary.total_scan_user if summary.total_scan_user > 0 else 0
            
        ])

    return response

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

def download_summary_as_csv_active_scan(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="SummaryScanHourInfo.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    header = [
        '통계일자','시간', '스캔_성공', '스캔_실패', '합계',
        '스캔 참여 회원 수', '인당 스캔 수', '스캔 비율_성공', '스캔 비율_실패', '평균 스캔 회원 수_성공', '평균 스캔 회원 수_실패'
    ]
    writer.writerow(header)

    summaries = SummaryScanHourInfo.objects.all()
    for summary in summaries:
        writer.writerow([
            summary.summary_dt,summary.summary_hour, summary.scan_success, summary.scan_fail,
            summary.scan_success + summary.scan_fail, summary.total_scan_user,
            (summary.scan_success + summary.scan_fail)/summary.total_scan_user if summary.total_scan_user > 0 else 0,
            summary.scan_success/(summary.scan_success + summary.scan_fail) * 100 if (summary.scan_success + summary.scan_fail) > 0 else 0,
            summary.scan_fail/(summary.scan_success + summary.scan_fail) * 100 if (summary.scan_success + summary.scan_fail) > 0 else 0,
            summary.scan_success/summary.total_scan_user if summary.total_scan_user > 0 else 0,
            summary.scan_fail/summary.total_scan_user if summary.total_scan_user > 0 else 0
            
        ])

    return response