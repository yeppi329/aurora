from django.db import models


# Create your models here.
# 스캔현황_월별현황
class SummaryScanMonthInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField("통계일자", max_length=255, blank=True)
    scan_success = models.BigIntegerField("스캔성공", default=0, blank=True)
    scan_fail = models.BigIntegerField("스캔실패", default=0, blank=True)
    total_scan_user = models.BigIntegerField("스캔참여회원", default=0, blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_scan_month_info"

    def __str__(self):
        return f"Scan ID: {self.summary_id}, Date: {self.summary_dt}"


# 스캔현황_일별현황
class SummaryScanDailyInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField("통계일자", max_length=255, blank=True)
    scan_success = models.BigIntegerField("스캔성공", default=0, blank=True)
    scan_fail = models.BigIntegerField("스캔실패", default=0, blank=True)
    total_scan_user = models.BigIntegerField("스캔참여회원", default=0, blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_scan_daily_info"

    def __str__(self):
        return f"Scan ID: {self.summary_id}, Date: {self.summary_dt}"


# 스캔현황_시간별현황
class SummaryScanHourInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField("통계일자", max_length=255, blank=True)
    scan_success = models.BigIntegerField("스캔성공", default=0, blank=True)
    scan_fail = models.BigIntegerField("스캔실패", default=0, blank=True)
    total_scan_user = models.BigIntegerField("스캔참여회원", default=0, blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "summary_scan_hour_info"

    def __str__(self):
        return f"Scan ID: {self.summary_id}, Date: {self.summary_dt}"


# 이용자현황_월별현황 + 대시보드 이용자 현황
class SummaryUserMonthInfo(models.Model):
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
        db_table = "summary_user_daily_info"

    def __str__(self):
        return f"Summary ID: {self.summary_id}, Date: {self.summary_dt}"


# class SummaryUserPeriodInfo(models.Model):
#     summary_id = models.BigAutoField(primary_key=True)
#     summary_dt = models.CharField(max_length=255, unique=True)
#     use_day_7 = models.BigIntegerField(default=0, blank=True)
#     use_day_30 = models.BigIntegerField(default=0, blank=True)
#     use_day_60 = models.BigIntegerField(default=0, blank=True)
#     use_day_90 = models.BigIntegerField(default=0, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True)

#     class Meta:
#         db_table = "summary_user_period_info"
#         managed = True

#     def __str__(self):
#         return f"Summary ID: {self.summary_id}, Date: {self.summary_dt}"


class SummaryUserTermInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255, unique=True)
    use_day_7 = models.BigIntegerField(default=0, blank=True)
    use_day_30 = models.BigIntegerField(default=0, blank=True)
    use_day_60 = models.BigIntegerField(default=0, blank=True)
    use_day_90 = models.BigIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "summary_user_term_info"

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
        return f"Summary ID: {self.summary_id}, Date: {self.reg_date}"
