from django.db import models

# Create your models here.
class SummaryScanInfo(models.Model):
    scan_id = models.BigAutoField(primary_key=True)
    reg_date = models.CharField(max_length=255)
    scan_success = models.BigIntegerField(default=0)
    scan_fail = models.BigIntegerField(default=0)
    scan_user = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'summary_scan_info'  

    def __str__(self):
        return f'Scan ID: {self.scan_id}, Date: {self.reg_date}'
    
class SummaryUserInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.CharField(max_length=255)
    total_user = models.BigIntegerField(default=0)
    new_user = models.BigIntegerField(default=0)
    suspended_user = models.BigIntegerField(default=0)
    deleted_user = models.BigIntegerField(default=0)
    return_user = models.BigIntegerField(default=0)
    inactive_user = models.BigIntegerField(default=0)
    dau = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'summary_user_info'  

    def __str__(self):
        return f'Summary ID: {self.summary_id}, Date: {self.summary_dt}'
       
class SummaryContentInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    reg_date = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255)
    content_cnt = models.BigIntegerField(default=0) #스캔,등록건수
    user_cnt = models.BigIntegerField(default=0)
    class Meta:
        db_table = 'summary_content_info'  

    def __str__(self):
        return f'Summary ID: {self.summary_id}, Date: {self.reg_date}'