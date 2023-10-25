from django.db import models


# Create your models here.
# 스캔현황_월별현황
class SummaryScanMonthInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField("통계일자", max_length=255, blank=True, unique=True)
    scan_success = models.BigIntegerField("스캔성공", default=0, blank=False)
    scan_fail = models.BigIntegerField("스캔실패", default=0, blank=False)
    total_scan_user = models.BigIntegerField("스캔참여회원", default=0, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_scan_month_info"

    def __str__(self):
        return f"Scan ID: {self.summary_id}, Date: {self.summary_dt}"


# 스캔현황_일별현황
class SummaryScanDailyInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField("통계일자", max_length=255, blank=False, unique=True)
    scan_success = models.BigIntegerField("스캔성공", default=0, blank=False)
    scan_fail = models.BigIntegerField("스캔실패", default=0, blank=False)
    total_scan_user = models.BigIntegerField("스캔참여회원", default=0, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_scan_daily_info"

    def __str__(self):
        return f"Scan ID: {self.summary_id}, Date: {self.summary_dt}"


# 스캔현황_시간별현황
class SummaryScanHourInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField("통계일자", max_length=255, blank=True)
    summary_hour = models.CharField("통계시간", max_length=255, blank=True)
    scan_success = models.BigIntegerField("스캔성공", default=0, blank=True)
    scan_fail = models.BigIntegerField("스캔실패", default=0, blank=True)
    total_scan_user = models.BigIntegerField("스캔참여회원", default=0, blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_scan_hour_info"
        unique_together = (("summary_dt", "summary_hour"),)

    def __str__(self):
        return f"Scan ID: {self.summary_id}, Date: {self.summary_dt}"


# 이용자현황_월별현황 + 대시보드 이용자 현황
class SummaryUserMonthInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField("통계일자", max_length=255, blank=True, unique=True)
    total_user = models.BigIntegerField(default=0, blank=True)
    new_user = models.BigIntegerField(default=0, blank=True)
    suspended_user = models.BigIntegerField(default=0, blank=True)
    deleted_user = models.BigIntegerField(default=0, blank=True)
    return_user = models.BigIntegerField(default=0, blank=True)
    inactive_user = models.BigIntegerField(default=0, blank=True)
    dau = models.BigIntegerField(default=0, blank=True)
    new_dau = models.BigIntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_user_month_info"

    def __str__(self):
        return f"Summary ID: {self.summary_id}, Date: {self.summary_dt}"


# 이용자현황_시간별현황 + 대시보드 이용자 현황
class SummaryUserHourInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField("통계일자", max_length=255, blank=True)
    total_user = models.BigIntegerField(default=0, blank=True)
    new_user = models.BigIntegerField(default=0, blank=True)
    suspended_user = models.BigIntegerField(default=0, blank=True)
    deleted_user = models.BigIntegerField(default=0, blank=True)
    return_user = models.BigIntegerField(default=0, blank=True)
    inactive_user = models.BigIntegerField(default=0, blank=True)
    dau = models.BigIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_user_hour_info"

    def __str__(self):
        return f"Summary ID: {self.summary_id}, Date: {self.summary_dt}"


# 이용자현황_일별현황 + 대시보드 이용자 현황
class SummaryUserDailyInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField("통계일자", max_length=255, blank=True, unique=True)
    total_user = models.BigIntegerField(default=0, blank=True)
    new_user = models.BigIntegerField(default=0, blank=True)
    suspended_user = models.BigIntegerField(default=0, blank=True)
    deleted_user = models.BigIntegerField(default=0, blank=True)
    return_user = models.BigIntegerField(default=0, blank=True)
    inactive_user = models.BigIntegerField(default=0, blank=True)
    dau = models.BigIntegerField(default=0, blank=True)
    new_dau = models.BigIntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_user_daily_info"

    def __str__(self):
        return f"Summary ID: {self.summary_id}, Date: {self.summary_dt}"


class SummaryUserPeriodInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255, unique=True)
    use_day_7 = models.BigIntegerField(default=0, blank=True)
    use_day_30 = models.BigIntegerField(default=0, blank=True)
    use_day_60 = models.BigIntegerField(default=0, blank=True)
    use_day_90 = models.BigIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "summary_user_period_info"

    def __str__(self):
        return f"Summary ID: {self.summary_id}, Date: {self.summary_dt}"


# 대시보드_콘텐츠현황
class SummaryContentInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField("통계일자", max_length=255, blank=True)
    content_type = models.CharField(max_length=255, blank=True)
    content_cnt = models.BigIntegerField(default=0, blank=True)  # 스캔,등록건수
    total_user = models.BigIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_content_info"

    def __str__(self):
        return f"Summary ID: {self.summary_id}, Date: {self.summary_dt}"

# 월별 컨텐츠 현황
class SummaryContentMonthInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255, null=False, blank=False, unique=True)     # 통계월 (YYYY-MM)
    post_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    post_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    media_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    media_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    arbecon_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    arbecon_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    drawing_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    drawing_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_content_month_info"

    def __str__(self):
        return f"Summary ID: {self.summary_id}, Date: {self.summary_dt}"


# 일별 컨텐츠 현황
class SummaryContentDailyInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255, null=False, blank=False, unique=True)     # 통계일 (YYYY-MM-DD)
    post_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    post_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    media_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    media_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    arbecon_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    arbecon_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    drawing_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    drawing_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_content_daily_info"

    def __str__(self):
        return f"Summary ID: {self.summary_id}, Date: {self.summary_dt}"

# 메뉴 퀀한 카테고리
class Category(models.Model):
    category_id = models.BigAutoField('카테고리 고유값', primary_key=True)
    parent_id = models.IntegerField('상위 카테고리 고유값', null=False, default=0)
    content_type = models.IntegerField('퍼미션 타입', null=False, default=0)
    category_name = models.CharField('카테고리 코드', max_length=255, blank=False)
    category_desc = models.CharField('카테고리 설명', max_length=255, blank=False)
    uri = models.CharField('카테고리 URI', max_length=255, blank=True)
    order = models.IntegerField('정렬순서', null=False, default=0)
    created_at = models.DateTimeField(auto_now=True, blank=True)

# 콘텐츠 상세 현황 (미디어)
class SummaryMediaDailyInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255, null=False, blank=False)     # 통계일 (YYYY-MM-DD)
    content_type = models.SmallIntegerField(null=False, blank=False, default=0)
    content_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    content_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    up_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    up_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    reply_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    reply_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_media_daily_info"
        unique_together = (("summary_dt", "content_type"),)

class SummaryMediaMonthInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255, null=False, blank=False)     # 통계일 (YYYY-MM)
    content_type = models.SmallIntegerField(null=False, blank=False, default=0)
    content_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    content_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    up_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    up_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    reply_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    reply_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_media_month_info"
        unique_together = (("summary_dt", "content_type"),)

# 콘텐츠 상세 현황 (알비콘)
class SummaryArbeconDailyInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255, null=False, blank=False)     # 통계일 (YYYY-MM-DD)
    resource_id = models.CharField(max_length=255, null=False, blank=False)
    content_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    content_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_arbecon_daily_info"
        unique_together = (("summary_dt", "resource_id"),)

class SummaryArbeconMonthInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255, null=False, blank=False)     # 통계일 (YYYY-MM)
    resource_id = models.CharField(max_length=255, null=False, blank=False)
    content_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    content_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_arbecon_month_info"
        unique_together = (("summary_dt", "resource_id"),)

# 콘텐츠 상세 현황 (드로잉)
class SummaryDrawingDailyInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255, null=False, blank=False)     # 통계일 (YYYY-MM-DD)
    drawing_type = models.SmallIntegerField(null=False, blank=False, default=0)
    content_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    content_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_drawing_daily_info"
        unique_together = (("summary_dt", "drawing_type"),)

class SummaryDrawingMonthInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255, null=False, blank=False)     # 통계일 (YYYY-MM-DD)
    drawing_type = models.SmallIntegerField(null=False, blank=False, default=0)
    content_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    content_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    like_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    share_user_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_drawing_month_info"
        unique_together = (("summary_dt", "drawing_type"),)

# 알비콘 리소스 코드
class ArbeconResource(models.Model):
    resource_id = models.CharField(primary_key=True, max_length=255, null=False, blank=False)
    motion_name = models.CharField(max_length=255, null=False, blank=False)
    show_name = models.CharField(max_length=255, null=False, blank=False)
    resource_desc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)