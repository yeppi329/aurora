from django.db import models

# Create your models here.
class SummaryScanInfo(models.Model):
    scan_id = models.BigAutoField(primary_key=True)
    reg_date = models.CharField(max_length=255)
    scan_success = models.BigIntegerField
    scan_fail = models.BigIntegerField
    scan_user = models.BigIntegerField

    class Meta:
        db_table = 'summary_scan_info'  

    def __str__(self):
        return f'Scan ID: {self.scan_id}, Date: {self.reg_date}'
    
class SummaryUserInfo(models.Model):
    summary_id = models.BigAutoField(primary_key=True)
    summary_dt = models.BigIntegerField
    total_user = models.BigIntegerField
    new_user = models.BigIntegerField
    suspended_user = models.BigIntegerField
    deleted_user = models.BigIntegerField
    return_user = models.BigIntegerField
    inactive_user = models.BigIntegerField
    dau = models.BigIntegerField

    class Meta:
        db_table = 'summary_user_info'  

    def __str__(self):
        return f'Summary ID: {self.summary_id}, Date: {self.summary_dt}'