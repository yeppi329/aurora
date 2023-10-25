from datetime import datetime
import random
import pandas as pd
import numpy as np
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from operation.models import (
    ScanInfo,
    ImageRecognition,
    Users,
    Content,
    Account,
    Report,
    Block,
    Media,
    Post,
)
from aurora.models import SummaryUserDailyInfo
from django.db.models import (
    OuterRef,
    Subquery,
    Count,
)
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
        mg_id_list = []
        for item in data:
            item.mg_id_count = int(item.mg_id_count or 0)
            mg_id_list.append(item.mg_id)
        mgId_shire_count_dict = esmodules.get_mgId_shire(mg_id_list)
        for item in data:
            item.shire_count = mgId_shire_count_dict[item.mg_id]

    elif object_type == "scan_id":
        scan_id_list = []
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
            scan_id_list.append(item["scan_id"])
        scanid_shire_dict = esmodules.get_doc_list(scan_id_list)
        for item in data:
            item["shire"] = scanid_shire_dict.get(item["scan_id"], None)
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

    total_count = queryset.count()
    # 원하는 페이지당 항목 수 설정
    items_per_page = 18  # 페이지당 15개 항목을 표시하도록 설정

    # Paginator를 사용하여 페이지네이션 객체 생성
    paginator = Paginator(queryset, items_per_page)
    # 페이지 번호 지정
    page_number = int(request.GET.get("page", 1))

    # 페이지 번호에 해당하는 Page 객체 가져오기
    page = paginator.get_page(page_number)

    scan_list = []
    user_id_list = []
    for _ in page:
        scan_list.append(_.scan_id)
        user_id_list.append(_.user_id)

    esmodules = EsModules()
    scanid_shire_dict = esmodules.get_doc_list(scan_list)

    # user_id, username
    matching_user_id = (
        Users.objects.using("lama")
        .filter(user_id__in=user_id_list)
        .values("user_id", "username")
    )
    matching_user_id_dict = {}
    for _ in matching_user_id:
        matching_user_id_dict[str(_["user_id"])] = _["username"]

    for _ in page:
        _.shire = scanid_shire_dict[_.scan_id]
        _.username = matching_user_id_dict.get(_.user_id, _.user_id)

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
        },
    )


@login_required(login_url="aurora:login")
def scanid_detail(request, scan_id):
    context = {"page_title": "mg ID 디테일 페이지"}
    esmodules = EsModules()
    es_result = esmodules.get_key_log(key=scan_id)
    content_data = []
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
        mg_id_list = []
        mg_id_list.append(query_result["mgId"])
        mg_id_list += query_result["simMgIdList"]
        # 하위 쿼리: mg_id와 content_type에 따른 content_id 목록을 가져옴
        content_ids = (
            Content.objects.using("pelican")
            .filter(mg_id__in=mg_id_list, content_type="MEDIA")
            .values_list("content_id", flat=True)
            .order_by("-created_at")
        )

        # 상위 쿼리: content_id가 하위 쿼리에서 가져온 목록에 있는 media 객체를 가져옴
        media_objects = (
            Media.objects.using("pelican")
            .filter(content_id__in=content_ids)
            .values("media_list")
        )

        for _ in media_objects:
            if _["media_list"]:
                content_data.append(_["media_list"][0])
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
            "content_data": content_data[:20],
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
    page_number = int(request.GET.get("page", 1))

    # 페이지 번호에 해당하는 Page 객체 가져오기
    page = paginator.get_page(page_number)

    scan_list = []
    user_id_list = []
    mg_id_list = []
    for _ in page:
        scan_list.append(_.scan_id)
        user_id_list.append(_.user_id)
        mg_id_list.append(_.mg_id)

    esmodules = EsModules()
    scanid_shire_dict = esmodules.get_doc_list(scan_list)

    # user_id, username
    matching_user_id = (
        Users.objects.using("lama")
        .filter(user_id__in=user_id_list)
        .values("user_id", "username")
    )
    matching_user_id_dict = {}
    for _ in matching_user_id:
        matching_user_id_dict[str(_["user_id"])] = _["username"]

    mg_id_list = list(set(mg_id_list))

    colors = [
        "red",
        "green",
        "blue",
        "yellow",
        "orange",
        "pink",
        "purple",
        "brown",
        "gray",
        "silver",
        "gold",
        "cyan",
        "magenta",
        "indigo",
        "violet",
        "aqua",
        "teal",
        "lavender",
        "maroon",
        "olive",
        "beige",
        "turquoise",
        "coral",
        "salmon",
        "plum",
        "orchid",
        "ruby",
        "pearl",
        "ebony",
        "ivory",
        "tangerine",
        "lemon",
        "mint",
        "lime",
        "peach",
        "charcoal",
        "mauve",
        "sepia",
        "amethyst",
        "periwinkle",
        "lilac",
        "celadon",
        "emerald",
        "chartreuse",
        "azure",
        "aquamarine",
        "cobalt",
        "sapphire",
        "garnet",
        "amber",
        "topaz",
        "bronze",
        "sienna",
        "terracotta",
        "sand",
        "khaki",
        "forest",
        "moss",
        "pine",
        "fern",
        "caramel",
        "cinnamon",
        "chestnut",
        "espresso",
        "walnut",
        "cognac",
        "taupe",
        "papaya",
        "blush",
        "rose",
        "fuchsia",
        "hotpink",
        "thistle",
        "wisteria",
        "grape",
        "eggplant",
        "olivedrab",
        "peru",
        "rosybrown",
        "slategray",
        "dodgerblue",
        "goldenrod",
        "tomato",
        "darkcyan",
        "mediumvioletred",
        "firebrick",
        "darkslategray",
        "mediumorchid",
        "royalblue",
        "darkorange",
        "darkseagreen",
        "cadetblue",
        "purple",
        "pink",
        "lightcoral",
    ]

    # 중복을 허용하지 않고 1:1로 매핑하기 위해 중복을 제거한 두 리스트의 길이 중 작은 길이를 사용
    min_length = min(len(mg_id_list), len(colors))

    # 중복을 제거한 컬러 리스트를 무작위로 섞음
    random.shuffle(colors)

    # 1:1로 매핑된 결과를 저장할 딕셔너리
    mapping_result = {}

    for i in range(min_length):
        mapping_result[mg_id_list[i]] = colors[i]

    print(mapping_result)
    for _ in page:
        _.shire = scanid_shire_dict[_.scan_id]
        _.color = mapping_result[_.mg_id]
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
        "aurora/pages/operation/object-list-user-id-detail.html",
        {
            "context": context,
            "user_id": user_id,
            "page": page,
            "total_count": total_count,
            "matching_user_id_dict": matching_user_id_dict,
            "crop_img_list": crop_img_list,
        },
    )


@login_required(login_url="aurora:login")
def new_mgid(request):
    context = {"page_title": "new mgid"}
    page_size = int(request.GET.get("page_size", 12))  # 기본값은 10입니다.
    page_number = int(request.GET.get("page", 1))
    esmodules = EsModules()
    page_number, last_page, total_count, new_mgid_data = esmodules.get_new_mgid(
        page_size, page_number
    )
    page_range = range(1, last_page + 1)
    if new_mgid_data:
        scan_id_list = [result["_id"] for result in new_mgid_data]
        scan_info_objects = (
            ScanInfo.objects.using("hippo")
            .filter(scan_id__in=scan_id_list)
            .values("scan_id", "img_url")
        )
        scanIdToImgUrlDict = {
            record["scan_id"]: record["img_url"] for record in scan_info_objects
        }
    data = []
    for _ in new_mgid_data:
        tmp = {}
        tmp["id"] = _["_id"]
        tmp["timestamp"] = datetime.strptime(
            _["_source"]["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        tmp["userId"] = _["_source"]["userId"]
        tmp["shire"] = _["_source"]["query-analysis-result"]["shire"]
        tmp["mgId"] = _["_source"]["query-analysis-result"]["mgId"]
        data.append(tmp)
    # user_id, username
    user_id_list = [result["userId"] for result in data]
    user_objects = (
        Users.objects.using("lama")
        .filter(user_id__in=user_id_list)
        .values("user_id", "username")
    )
    matching_user_id_dict = {}
    for _ in user_objects:
        matching_user_id_dict[str(_["user_id"])] = _["username"]
    return render(
        request,
        "aurora/pages/operation/new-mg-id.html",
        {
            "context": context,
            "page_size": page_size,
            "page_number": page_number,
            "last_page": last_page,
            "page_range": page_range,
            "total_count": total_count,
            "data": data,
            "scanIdToImgUrlDict": scanIdToImgUrlDict,
            "matching_user_id_dict": matching_user_id_dict,
        },
    )


@login_required(login_url="aurora:login")
def new_mgid_detail(request, scan_id):
    context = {"page_title": "new_mgid_detail"}
    data_size = int(request.GET.get("data_size", 20))
    esmodules = EsModules()
    scan_id_data = esmodules.es.get(index=esmodules.search_index, id=scan_id)
    type_ = choice_type(scan_id_data["_source"]["shire"])
    mgid = scan_id_data["_source"]["mgId"]
    last_processed_timestamp = scan_id_data["_source"]["@timestamp"]
    emb = scan_id_data["_source"][type_]
    gps = scan_id_data["_source"]["geohash"]

    query_data = {
        "mgId": mgid,
        "timestamp": datetime.strptime(
            last_processed_timestamp, "%Y-%m-%dT%H:%M:%S.%fZ"
        ),
        "shire": scan_id_data["_source"]["shire"],
        "userId": scan_id_data["_source"]["userId"],
        "gps": gps,
    }
    query = esmodules.embedding_query(
        type_=type_,
        embedding=emb,
        last_processed_timestamp=last_processed_timestamp,
        data_size=data_size,
        geohash=gps,
    )
    if type_:
        search_result_raw = esmodules.search(query_body=query)["hits"]["hits"]

    search_result = []
    for _ in search_result_raw:
        tmp = {}
        tmp["scan_id"] = _["_id"]
        tmp["score"] = _["_score"]
        tmp["mgId"] = _["_source"]["mgId"]
        tmp["userId"] = _["_source"]["userId"]
        tmp["shire"] = _["_source"]["shire"]
        tmp["timestamp"] = datetime.strptime(
            _["_source"]["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        search_result.append(tmp)

    scan_id_list = [result["scan_id"] for result in search_result]
    scan_id_list.append(scan_id)
    scan_info_objects = (
        ScanInfo.objects.using("hippo")
        .filter(scan_id__in=scan_id_list)
        .values("scan_id", "img_url")
    )
    scanIdToImgUrlDict = {
        record["scan_id"]: record["img_url"] for record in scan_info_objects
    }

    if scan_id_data["_source"]:
        crop_data = {}
        crop_data["cropX"] = scan_id_data["_source"]["crop.cropX"]
        crop_data["cropY"] = scan_id_data["_source"]["crop.cropY"]
        crop_data["cropW"] = scan_id_data["_source"]["crop.cropW"]
        crop_data["cropH"] = scan_id_data["_source"]["crop.cropH"]
        crop_img = show_draw_crop(scanIdToImgUrlDict[scan_id], crop_data)
    else:
        crop_img = None
    # user_id, username
    user_id_list = [
        result["userId"]
        for result in search_result
        if is_valid_uuid(result.get("userId"))
    ]
    user_id_list.append(scan_id_data["_source"]["userId"])
    user_objects = (
        Users.objects.using("lama")
        .filter(user_id__in=user_id_list)
        .values("user_id", "username")
    )
    matching_user_id_dict = {}
    for _ in user_objects:
        matching_user_id_dict[str(_["user_id"])] = _["username"]

    return render(
        request,
        "aurora/pages/operation/new-mg-id-detail.html",
        {
            "context": context,
            "scan_id": scan_id,
            "data_size": data_size,
            "query_data": query_data,
            "search_result": search_result,
            "scanIdToImgUrlDict": scanIdToImgUrlDict,
            "matching_user_id_dict": matching_user_id_dict,
            "crop_img": crop_img,
        },
    )


# 유저관리
@login_required(login_url="aurora:login")
def user_management(request):
    context = {"page_title": "이용자 관리"}
    header_data = SummaryUserDailyInfo.objects.latest("created_at")
    ###
    status = request.GET.get("status")

    if not status:
        account_data = Account.objects.using("camel").values().order_by("-created_at")
    elif status == "1":
        account_data = (
            Account.objects.using("camel")
            .filter(status=1)
            .values()
            .order_by("-created_at")
        )
    elif status == "0":
        account_data = (
            Account.objects.using("camel")
            .filter(status=0)
            .values()
            .order_by("-created_at")
        )
    elif status == "99":
        account_data = (
            Account.objects.using("camel")
            .filter(status=99)
            .values()
            .order_by("-created_at")
        )
    else:
        account_data = Account.objects.using("camel").values().order_by("-created_at")
    q = request.GET.get("q")
    st = request.GET.get("st")
    if q and st:
        if st == "email":
            account_data = (
                Account.objects.using("camel")
                .filter(email=q)
                .values()
                .order_by("-created_at")
            )
        else:
            username_data = (
                Users.objects.using("lama").filter(username=q).order_by("-created_at")
            )
            search_account_list = []
            for _ in username_data:
                search_account_list.append(_.account_id)
            account_data = (
                Account.objects.using("camel")
                .values()
                .filter(account_id__in=search_account_list)
            )

    page_size = int(request.GET.get("page_size", 10))  # 기본값은 10입니다.
    page_number = int(request.GET.get("page", 1))
    # Paginator를 사용하여 페이지네이션 객체 생성
    paginator = Paginator(account_data, page_size)

    # 페이지 번호에 해당하는 Page 객체 가져오기
    page = paginator.get_page(page_number)
    account_data = pd.DataFrame(list(page))
    if list(page):
        # find user id
        matching_user_id = (
            Users.objects.using("lama")
            .filter(account_id__in=list(account_data["account_id"]))
            .values("user_id", "account_id", "username")
        )
        user_data = pd.DataFrame(list(matching_user_id))
        if len(user_data):
            result = pd.merge(account_data, user_data, on="account_id", how="left")

            # Content Count
            content_count = (
                Content.objects.using("pelican")
                .filter(user_id__in=list(result["user_id"]))
                .values("user_id")
                .annotate(content_count=Count("user_id"))
            )
            content_count_data = pd.DataFrame(list(content_count))
            if list(content_count_data):
                content_count_data["user_id"] = content_count_data["user_id"].apply(
                    lambda x: uuid.UUID(x)
                )

                result = pd.merge(result, content_count_data, on="user_id", how="left")
                result.fillna(0, inplace=True)
                result["content_count"] = result["content_count"].apply(
                    lambda x: int(x)
                )
            # 조건에 따라 count 값을 설정
            conditions = [
                (result["status"] == 0),
                (result["status"] == 1),
                (result["status"] == 99),
            ]

            values = ["정지", "정상", "탈퇴"]
            result["status_str"] = np.select(conditions, values, default="")
            return render(
                request,
                "aurora/pages/operation/user-management.html",
                {
                    "context": context,
                    "header_data": header_data,
                    "status": status,
                    "page_size": page_size,
                    "page_number": page_number,
                    "data": result.to_dict(orient="records"),
                    "page": page,
                },
            )
        else:
            return render(
                request,
                "aurora/pages/operation/user-management.html",
                {
                    "context": context,
                    "header_data": header_data,
                    "status": status,
                    "page_size": page_size,
                    "page_number": page_number,
                    "data": account_data.to_dict(orient="records"),
                    "page": page,
                },
            )

    else:
        return render(
            request,
            "aurora/pages/operation/user-management.html",
            {
                "context": context,
                "header_data": header_data,
                "status": status,
                "page_size": page_size,
                "page_number": page_number,
                "data": account_data.to_dict(orient="records"),
                "page": page,
            },
        )


@login_required(login_url="aurora:login")
def accountid_detail(request, account_id):
    context = {"page_title": "유저 계정정보 디테일 페이지"}
    account_data = (
        Account.objects.using("camel").filter(account_id=account_id).values()[0]
    )
    user_data = Users.objects.using("lama").filter(account_id=account_id).values()[0]
    report_count = (
        Report.objects.using("lama").filter(user_id=user_data["user_id"]).count()
    )
    block_count = (
        Block.objects.using("lama").filter(user_id=user_data["user_id"]).count()
    )

    scan_info_data = []
    fail_count = (
        ScanInfo.objects.using("hippo")
        .filter(user_id=user_data["user_id"])
        .filter(mg_id="")
        .count()
    )
    fail_count_dict = {"label": "fail", "serie": fail_count}
    scan_info_data.append(fail_count_dict)
    success_count = (
        ScanInfo.objects.using("hippo")
        .filter(user_id=user_data["user_id"])
        .exclude(mg_id="")
        .count()
    )
    success_count_dict = {"label": "success", "serie": success_count}
    scan_info_data.append(success_count_dict)

    content_ids = (
        Content.objects.using("pelican")
        .filter(user_id=user_data["user_id"])
        .values_list("content_id", flat=True)
    )
    card_info_data = list(
        Media.objects.using("pelican")
        .filter(content_id__in=content_ids)
        .values("type")
        .annotate(serie=Count("type"))
    )
    for item in card_info_data:
        item["label"] = item.pop("type")
    content_type_info_data = list(
        Content.objects.using("pelican")
        .filter(user_id=user_data["user_id"])
        .values("content_type")
        .annotate(serie=Count("content_type"))
    )
    for item in content_type_info_data:
        item["label"] = item.pop("content_type")

    etc_content_info_data = list(
        Content.objects.using("pelican")
        .filter(user_id=user_data["user_id"])
        .values("comment_cnt", "like_cnt", "up_cnt")
    )
    print("*" * 20)
    comment_cnt = 0
    like_cnt = 0
    up_cnt = 0
    for _ in etc_content_info_data:
        comment_cnt += _["comment_cnt"]
        like_cnt += _["like_cnt"]
        up_cnt += _["up_cnt"]

    post_cnt = (
        Post.objects.using("pelican")
        .filter(user_id=user_data["user_id"])
        .values("user_id")
        .count()
    )

    ratio = post_cnt + comment_cnt + like_cnt + up_cnt
    if ratio != 0:
        post_ratio = post_cnt / ratio * 100
        comment_ratio = comment_cnt / ratio * 100
        like_ratio = like_cnt / ratio * 100
        up_ratio = up_cnt / ratio * 100
    else:
        post_ratio = 0
        comment_ratio = 0
        like_ratio = 0
        up_ratio = 0

    etc_info_data = {
        "post_cnt": post_cnt,
        "post_ratio": post_ratio,
        "comment_cnt": comment_cnt,
        "comment_ratio": comment_ratio,
        "like_cnt": like_cnt,
        "like_ratio": like_ratio,
        "up_cnt": up_cnt,
        "up_ratio": up_ratio,
    }
    return render(
        request,
        "aurora/pages/operation/user-management-account-id-detail.html",
        {
            "context": context,
            "account_id": account_id,
            "account_data": account_data,
            "user_data": user_data,
            "report_count": report_count,
            "block_count": block_count,
            "scan_info_data": scan_info_data,
            "card_info_data": card_info_data,
            "content_type_info_data": content_type_info_data,
            "etc_info_data": etc_info_data,
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
