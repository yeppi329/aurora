from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ScanInfo, ImageRecognition
from django.db.models import OuterRef, Subquery, Count, Max, F, Min
from django.db import connections
from django.core.paginator import Paginator
import time
from .utils import *


@login_required(login_url="aurora:login")
def index(request):
    context = {"page_title": "이용자 관리"}
    return render(request, "aurora/pages/operation/svc-user-list.html", context)


@login_required(login_url="aurora:login")
def svc_user_list(request):
    context = {"page_title": "이용자 관리"}
    return render(request, "aurora/pages/operation/svc-user-list.html", context)


@login_required(login_url="aurora:login")
def object_list(request, object_type="mg_id"):
    context = {"page_title": "사물 관리"}
    print(object_type)
    # header data
    # count mg_id
    unique_count_mg_id = (
        ScanInfo.objects.using("hippo_db").values("mg_id").distinct().count()
    )
    # count total scan_id
    total_count_sacn_id = ScanInfo.objects.using("hippo_db").count()

    # count unique user
    unique_count_user_id = (
        ScanInfo.objects.using("hippo_db").values("user_id").distinct().count()
    )

    if object_type == "mg_id":
        # mg_id 별로 레코드 수와 img_url을 가져오는 서브쿼리
        record_count_subquery = (
            ScanInfo.objects.using("hippo_db")
            .values("mg_id")
            .annotate(mg_id_count=Count("mg_id"))
        )

        # ImageRecognition 모델에서 first_scan_id를 통해 mg_id_count와 img_url을 가져옵니다.
        data = ImageRecognition.objects.using("hippo_db").annotate(
            mg_id_count=Subquery(
                record_count_subquery.filter(mg_id=OuterRef("mg_id")).values(
                    "mg_id_count"
                )
            ),
            img_url=Subquery(
                ScanInfo.objects.using("hippo_db")
                .filter(scan_id=OuterRef("first_scan_id"))
                .values("img_url")
            ),
        )
    else:
        matching_image_url = (
            ScanInfo.objects.using("hippo_db")
            .order_by("mg_id", "created_at")
            .distinct("mg_id")
            .values("mg_id", "img_url")
        )
        # ScanInfo 모델을 사용하여 쿼리 생성
        data = (
            ScanInfo.objects.using("hippo_db")
            .values()
            .order_by("-created_at")
            .annotate(
                frist_img_url=Subquery(
                    matching_image_url.filter(mg_id=OuterRef("mg_id")).values("img_url")
                )
            )
        )
        print(data)

    return render(
        request,
        "aurora/pages/operation/object-list.html",
        {
            "context": context,
            "object_type": object_type,
            "unique_count_mg_id": unique_count_mg_id,
            "total_count_sacn_id": total_count_sacn_id,
            "unique_count_user_id": unique_count_user_id,
            "data": data,
        },
    )


@login_required(login_url="aurora:login")
def mgid_detail(request, mg_id):
    context = {"page_title": "mg ID 디테일 페이지"}
    # ScanInfo 모델을 사용하여 쿼리 생성
    mg_id_like_cnt = (
        ImageRecognition.objects.using("hippo_db")
        .filter(mg_id=mg_id)
        .values("like_cnt")
    )
    # ScanInfo 모델을 사용하여 쿼리 생성
    queryset = (
        ScanInfo.objects.using("hippo_db").filter(mg_id=mg_id).order_by("created_at")
    )
    # 원하는 페이지당 항목 수 설정
    items_per_page = 15  # 페이지당 15개 항목을 표시하도록 설정

    # Paginator를 사용하여 페이지네이션 객체 생성
    paginator = Paginator(queryset, items_per_page)
    # 페이지 번호 지정
    page_number = request.GET.get("page")  # URL 매개변수에서 페이지 번호를 가져옴

    # 페이지 번호가 없는 경우 기본값을 설정할 수 있습니다.
    if not page_number:
        page_number = 1
    # 페이지 번호에 해당하는 Page 객체 가져오기
    page = paginator.get_page(page_number)
    return render(
        request,
        "aurora/pages/operation/object-list-mg-id-detail.html",
        {
            "context": context,
            "mg_id": mg_id,
            "page": page,
            "mg_id_like_cnt": mg_id_like_cnt,
        },
    )


@login_required(login_url="aurora:login")
def scanid_detail(request, scan_id):
    context = {"page_title": "mg ID 디테일 페이지"}
    # uuid_obj를 사용하여 원하는 작업을 수행할 수 있습니다.
    response = f"scan_id 값: {scan_id}"
    print(response)
    return render(
        request,
        "aurora/pages/operation/object-list-scan-id-detail.html",
        {
            "scan_id": scan_id,
        },
    )


@login_required(login_url="aurora:login")
def content_list(request):
    context = {"page_title": "이용자 관리"}
    return render(request, "aurora/pages/operation/content-list.html", context)


@login_required(login_url="aurora:login")
def report_list(request):
    context = {"page_title": "사물 관리"}
    return render(request, "aurora/pages/operation/report-list.html", context)


# Create your views here.
