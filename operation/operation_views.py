from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ScanInfo, ImageRecognition
from django.db.models import OuterRef, Subquery
from django.db import connections

import time


@login_required(login_url="aurora:login")
def index(request):
    context = {"page_title": "이용자 관리"}
    return render(request, "aurora/pages/operation/svc-user-list.html", context)


@login_required(login_url="aurora:login")
def svc_user_list(request):
    context = {"page_title": "이용자 관리"}
    return render(request, "aurora/pages/operation/svc-user-list.html", context)


@login_required(login_url="aurora:login")
def object_list(request):
    context = {"page_title": "사물 관리"}
    # # 1번 방법
    # # ImageRecognition 테이블에서 각 mg_id에 대한 like_cnt를 서브쿼리로 가져옵니다.
    # start_time = time.time()
    # image_recognition_subquery = (
    #     ImageRecognition.objects.using("hippo_db")
    #     .filter(mg_id=OuterRef("mg_id"))
    #     .values("like_cnt", "first_scan_id")
    # )

    # # ScanInfo 모델에 서브쿼리 결과를 병합합니다.
    # scan_info_query = (
    #     ScanInfo.objects.using("hippo_db")
    #     .annotate(
    #         like_cnt=Subquery(image_recognition_subquery.values("like_cnt")),
    #         first_scan_id=Subquery(image_recognition_subquery.values("first_scan_id")),
    #     )
    #     .order_by("-created_at")
    #     .values(
    #         "scan_id",
    #         "mg_id",
    #         "img_url",
    #         "crop_img_url",
    #         "meta_data",
    #         "user_id",
    #         "geohash",
    #         "created_at",
    #         "updated_at",
    #         "deleted_at",
    #         "status_flag",
    #         "img_name",
    #         "enc_geo",
    #         "like_cnt",  # ImageRecognition의 like_cnt 필드
    #         "first_scan_id",
    #     )
    # )

    # # 결과를 리스트로 변환하거나 다른 형태로 처리할 수 있습니다.
    # data = list(scan_info_query)
    # for item in data:
    #     first_scan_id = item.get("first_scan_id")
    #     if first_scan_id:
    #         first_scan_info = ScanInfo.objects.using("hippo_db").get(
    #             scan_id=first_scan_id
    #         )
    #         item["first_scan_img_url"] = first_scan_info.img_url
    # end_time = time.time()
    # execution_time = end_time - start_time
    # print(f"실행 시간: {execution_time:.5f} 초")

    #############################################
    # 2번방법
    # ImageRecognition 테이블에서 각 mg_id에 대한 like_cnt와 first_scan_id를 서브쿼리로 가져옵니다.
    start_time = time.time()
    image_recognition_subquery = (
        ImageRecognition.objects.using("hippo_db")
        .filter(mg_id=OuterRef("mg_id"))
        .values("like_cnt", "first_scan_id")
    )

    # ScanInfo 모델에 서브쿼리 결과를 병합합니다.
    scan_info_query = (
        ScanInfo.objects.using("hippo_db")
        .annotate(
            like_cnt=Subquery(image_recognition_subquery.values("like_cnt")),
            first_scan_id=Subquery(image_recognition_subquery.values("first_scan_id")),
        )
        .order_by("-created_at")
        .values(
            "scan_id",
            "mg_id",
            "img_url",
            "crop_img_url",
            "meta_data",
            "user_id",
            "geohash",
            "created_at",
            "updated_at",
            "deleted_at",
            "status_flag",
            "img_name",
            "enc_geo",
            "like_cnt",  # ImageRecognition의 like_cnt 필드
            "first_scan_id",  # ImageRecognition의 first_scan_id 필드
        )
    )

    # first_scan_id를 사용하여 first_scan_img_url을 가져옵니다.
    first_scan_img_url_subquery = (
        ScanInfo.objects.using("hippo_db")
        .filter(scan_id=OuterRef("first_scan_id"))
        .values("img_url")[:1]
    )

    scan_info_query = scan_info_query.annotate(
        first_scan_img_url=Subquery(first_scan_img_url_subquery)
    )

    # 결과를 리스트로 변환하거나 다른 형태로 처리할 수 있습니다.
    data = list(scan_info_query)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"실행 시간: {execution_time:.5f} 초")

    ##############################################
    # # 3번방법 원시쿼리 -> 이건 다시 객체화해줘야됨... (귀찬)
    # # 데이터베이스 연결을 가져옵니다.
    # start_time = time.time()
    # with connections["hippo_db"].cursor() as cursor:
    #     # 실행할 SQL 쿼리를 작성합니다.
    #     sql_query = """
    #         SELECT scan_info.*,
    #             image_recognition.like_cnt,
    #             (
    #                 SELECT img_url
    #                 FROM scan_info AS si
    #                 WHERE si.scan_id = image_recognition.first_scan_id
    #             ) AS first_scan_img_url
    #         FROM scan_info
    #         LEFT JOIN image_recognition ON scan_info.mg_id = image_recognition.mg_id
    #         ORDER BY scan_info.created_at DESC;
    #     """

    #     # SQL 쿼리를 실행합니다.
    #     cursor.execute(sql_query)

    #     # 결과를 가져옵니다.
    #     data = cursor.fetchall()
    # print(data[0])
    # # 결과를 처리하거나 반환합니다.
    # end_time = time.time()
    # execution_time = end_time - start_time
    # print(f"실행 시간: {execution_time:.5f} 초")
    return render(request, "aurora/pages/operation/object-list.html", {"data": data})


@login_required(login_url="aurora:login")
def content_list(request):
    context = {"page_title": "이용자 관리"}
    return render(request, "aurora/pages/operation/content-list.html", context)


@login_required(login_url="aurora:login")
def report_list(request):
    context = {"page_title": "사물 관리"}
    return render(request, "aurora/pages/operation/report-list.html", context)


# Create your views here.
