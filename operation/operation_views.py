from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ScanInfo, ImageRecognition, Users
from django.db.models import OuterRef, Subquery, Count, Q, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
from .utils import *
import json
from .es_models import EsModules

import concurrent.futures


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
    # count mg_id
    unique_count_mg_id = (
        ScanInfo.objects.using("hippo").values("mg_id").distinct().count()
    )
    # count total scan_id
    total_count_sacn_id = ScanInfo.objects.using("hippo").count()

    # count unique user
    unique_count_user_id = (
        ScanInfo.objects.using("hippo").values("user_id").distinct().count()
    )

    # count category
    esmodules = EsModules()
    es_result = esmodules.get_category()
    category_data = {}
    for bucket in es_result:
        key = bucket.get("key", "")
        doc_count = bucket.get("doc_count", 0)
        category_data[key] = doc_count
    # JSON 데이터를 문자열로 변환
    category_data_json = json.dumps(category_data)

    if object_type == "mg_id":
        # mg_id 별로 레코드 수와 img_url을 가져오는 서브쿼리
        record_count_subquery = (
            ScanInfo.objects.using("hippo")
            .values("mg_id")
            .annotate(mg_id_count=Count("mg_id"))
        )

        # ImageRecognition 모델에서 first_scan_id를 통해 mg_id_count와 img_url을 가져옵니다.
        data_query = (
            ImageRecognition.objects.using("hippo")
            .annotate(
                mg_id_count=Subquery(
                    record_count_subquery.filter(mg_id=OuterRef("mg_id")).values(
                        "mg_id_count"
                    )
                ),
                img_url=Subquery(
                    ScanInfo.objects.using("hippo")
                    .filter(scan_id=OuterRef("first_scan_id"))
                    .values("img_url")
                ),
            )
            .order_by("-created_at")
        )
    elif object_type == "scan_id":
        matching_image_url = (
            ScanInfo.objects.using("hippo")
            .order_by("mg_id", "created_at")
            .distinct("mg_id")
            .values("mg_id", "img_url")
        )
        matching_user_id = Users.objects.using("lama").values("user_id", "username")
        # ScanInfo 모델을 사용하여 쿼리 생성
        data_query = (
            ScanInfo.objects.using("hippo")
            .values()
            .order_by("-created_at")
            .annotate(
                frist_img_url=Subquery(
                    matching_image_url.filter(mg_id=OuterRef("mg_id")).values("img_url")
                ),
            )
        )
    else:
        # 서브쿼리로서 record_count_subquery를 준비합니다.
        record_count_subquery = (
            ScanInfo.objects.using("hippo")
            .filter(user_id=OuterRef("user_id"))
            .values("user_id")
            .annotate(user_id_count=Count("user_id"))
            .values("user_id_count")
        )

        matching_user_id = Users.objects.using("lama").values("user_id", "username")
        # user_data를 가져오고 외부 조인합니다.
        data_query = (
            ScanInfo.objects.using("hippo")
            .values()
            .order_by("user_id", "-created_at")
            .distinct("user_id")
            .annotate(user_id_count=Subquery(record_count_subquery))
        )

    page_size = int(request.GET.get("page_size", 10))  # 기본값은 10입니다.
    # Paginator 객체를 생성합니다.
    paginator = Paginator(data_query, page_size)

    # 요청한 페이지 번호를 가져옵니다. 일반적으로 GET 요청에서 페이지 번호를 가져옵니다.
    page_number = request.GET.get("page")

    try:
        # 요청한 페이지 번호에 해당하는 페이지 객체를 가져옵니다.
        data = paginator.page(page_number)
    except PageNotAnInteger:
        # 페이지 번호가 정수가 아닌 경우, 첫 번째 페이지를 가져옵니다.
        data = paginator.page(1)
    except EmptyPage:
        # 페이지 번호가 범위를 벗어난 경우, 마지막 페이지를 가져옵니다.
        data = paginator.page(paginator.num_pages)

    if object_type == "mg_id":
        for item in data:
            item.mg_id_count = int(item.mg_id_count or 0)
    elif object_type == "scan_id":
        for item in data:
            user_id = item["user_id"]
            matching_username = next(
                (
                    user["username"]
                    for user in matching_user_id
                    if str(user["user_id"]) == user_id
                ),
                None,
            )
            item["username"] = matching_username
    else:
        for item in data:
            item["user_id_count"] = int(item["user_id_count"] or 0)
            user_id = item["user_id"]
            matching_username = next(
                (
                    user["username"]
                    for user in matching_user_id
                    if str(user["user_id"]) == user_id
                ),
                None,
            )
            item["username"] = matching_username

    return render(
        request,
        "aurora/pages/operation/object-list.html",
        {
            "context": context,
            "object_type": object_type,
            "unique_count_mg_id": unique_count_mg_id,
            "total_count_sacn_id": total_count_sacn_id,
            "unique_count_user_id": unique_count_user_id,
            "category_data": category_data,
            "category_data_json": category_data_json,
            "data": data,
            "page_number": page_number,
            "page_size": page_size,
        },
    )


@login_required(login_url="aurora:login")
def mgid_detail(request, mg_id):
    context = {"page_title": "mg ID 디테일 페이지"}
    # ScanInfo 모델을 사용하여 쿼리 생성
    mg_id_like_cnt = (
        ImageRecognition.objects.using("hippo").filter(mg_id=mg_id).values("like_cnt")
    )
    # ScanInfo 모델을 사용하여 쿼리 생성
    queryset = (
        ScanInfo.objects.using("hippo").filter(mg_id=mg_id).order_by("created_at")
    )

    # user_id, username
    matching_user_id = Users.objects.using("lama").values("user_id", "username")
    matching_user_id_dict = {}
    for _ in matching_user_id:
        matching_user_id_dict[str(_["user_id"])] = _["username"]

    total_count = queryset.count()
    # 원하는 페이지당 항목 수 설정
    items_per_page = 18  # 페이지당 15개 항목을 표시하도록 설정

    # Paginator를 사용하여 페이지네이션 객체 생성
    paginator = Paginator(queryset, items_per_page)
    # 페이지 번호 지정
    page_number = request.GET.get("page")  # URL 매개변수에서 페이지 번호를 가져옴

    # 페이지 번호가 없는 경우 기본값을 설정할 수 있습니다.
    if not page_number:
        page_number = 1
    # 페이지 번호에 해당하는 Page 객체 가져오기
    page = paginator.get_page(page_number)

    # # 일반
    # start_time = time.time()
    # crop_img_list = {}
    # for _ in page:
    #     crop_img = show_draw_crop(_.img_url, _.meta_data)
    #     crop_img_list[_.scan_id] = crop_img
    # end_time = time.time()
    # # 실행 시간 계산 (종료 시간 - 시작 시간)
    # execution_time = end_time - start_time

    # # 실행 시간 출력
    # print(f"일반: {execution_time} seconds")

    # 멀티스레드
    start_time = time.time()
    crop_img_list = {}

    # 멀티스레딩으로 이미지 처리 함수를 병렬로 실행
    def process_page(page_item):
        crop_img = show_draw_crop(page_item.img_url, page_item.meta_data)
        crop_img_list[page_item.scan_id] = crop_img

    # 스레드 풀 생성
    max_threads = 4  # 최대 스레드 수 (조정 가능)
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        # 페이지의 각 항목을 처리하는 스레드를 스케줄링
        executor.map(process_page, page)

    end_time = time.time()
    # 실행 시간 계산 (종료 시간 - 시작 시간)
    execution_time = end_time - start_time
    print(f"멀티스레딩 : {execution_time} seconds")
    return render(
        request,
        "aurora/pages/operation/object-list-mg-id-detail.html",
        {
            "context": context,
            "mg_id": mg_id,
            "total_count": total_count,
            "page": page,
            "mg_id_like_cnt": mg_id_like_cnt,
            "crop_img_list": crop_img_list,
            "matching_user_id_dict": matching_user_id_dict,
        },
    )


@login_required(login_url="aurora:login")
def scanid_detail(request, scan_id):
    context = {"page_title": "mg ID 디테일 페이지"}
    # uuid_obj를 사용하여 원하는 작업을 수행할 수 있습니다.
    response = f"scan_id 값: {scan_id}"
    esmodules = EsModules()
    es_result = esmodules.get_key_log(key=scan_id)

    if es_result["hits"]["total"]["value"] > 0:
        query_result = es_result["hits"]["hits"][0]["_source"]["query-analysis-result"]
        search_result = es_result["hits"]["hits"][0]["_source"]["search-results"]
        scan_id_list = [result["scanId"] for result in search_result]
        scan_id_list.append(scan_id)
        scan_info_objects = (
            ScanInfo.objects.using("hippo")
            .filter(scan_id__in=scan_id_list)
            .values("scan_id", "img_url")
        )
        scanIdToImgUrlDict = {
            record["scan_id"]: record["img_url"] for record in scan_info_objects
        }
    else:
        # es_result에 검색 결과가 없는 경우에 대한 처리
        query_result = None
        search_result = None
        scan_id_list = []
        scan_id_list.append(scan_id)
        scan_info_objects = (
            ScanInfo.objects.using("hippo")
            .filter(scan_id__in=scan_id_list)
            .values("scan_id", "img_url")
        )
        scanIdToImgUrlDict = {
            record["scan_id"]: record["img_url"] for record in scan_info_objects
        }

    ###
    scan_img_url = scanIdToImgUrlDict[scan_id]
    if query_result:
        crop_data = {}
        crop_data["cropX"] = query_result["crop.cropX"]
        crop_data["cropY"] = query_result["crop.cropY"]
        crop_data["cropW"] = query_result["crop.cropW"]
        crop_data["cropH"] = query_result["crop.cropH"]
        crop_img = show_draw_crop(scan_img_url, crop_data)
    else:
        crop_img = None

    return render(
        request,
        "aurora/pages/operation/object-list-scan-id-detail.html",
        {
            "context": context,
            "scan_id": scan_id,
            "crop_img": crop_img,
            "query_result": query_result,
            "search_result": search_result,
            "scanIdToImgUrlDict": scanIdToImgUrlDict,
        },
    )


@login_required(login_url="aurora:login")
def userid_detail(request, user_id):
    context = {"page_title": "유저아이디 디테일 페이지"}
    # ScanInfo 모델을 사용하여 쿼리 생성
    queryset = (
        ScanInfo.objects.using("hippo").filter(user_id=user_id).order_by("-created_at")
    )
    total_count = queryset.count()
    # 원하는 페이지당 항목 수 설정
    items_per_page = 18  # 페이지당 15개 항목을 표시하도록 설정

    # Paginator를 사용하여 페이지네이션 객체 생성
    paginator = Paginator(queryset, items_per_page)
    # 페이지 번호 지정
    page_number = request.GET.get("page")  # URL 매개변수에서 페이지 번호를 가져옴

    # 페이지 번호가 없는 경우 기본값을 설정할 수 있습니다.
    if not page_number:
        page_number = 1
    # 페이지 번호에 해당하는 Page 객체 가져오기
    page = paginator.get_page(page_number)
    # user_id, username
    matching_user_id = Users.objects.using("lama").values("user_id", "username")
    matching_user_id_dict = {}
    for _ in matching_user_id:
        matching_user_id_dict[str(_["user_id"])] = _["username"]

    return render(
        request,
        "aurora/pages/operation/object-list-user-id-detail.html",
        {
            "context": context,
            "user_id": user_id,
            "page": page,
            "total_count": total_count,
            "matching_user_id_dict": matching_user_id_dict,
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
