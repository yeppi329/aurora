# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brand(models.Model):
    brand_id = models.CharField(primary_key=True, max_length=-1)
    brand_name = models.CharField(max_length=-1, blank=True, null=True)
    brand_image_url = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand'


class FlywaySchemaHistory(models.Model):
    installed_rank = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'flyway_schema_history'


class Goods(models.Model):
    goods_id = models.CharField(primary_key=True, max_length=-1)
    goods_name = models.CharField(max_length=-1, blank=True, null=True)
    goods_desc = models.CharField(max_length=-1, blank=True, null=True)
    goods_img = models.CharField(max_length=-1, blank=True, null=True)
    goods_price = models.IntegerField(blank=True, null=True)
    goods_ref = models.CharField(max_length=-1, blank=True, null=True)
    goods_category = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    mg_id = models.CharField(max_length=-1, blank=True, null=True)
    discount_price = models.IntegerField(blank=True, null=True)
    discount_flag = models.BooleanField(blank=True, null=True)
    ci_logo = models.CharField(max_length=-1, blank=True, null=True)
    middle_category = models.CharField(max_length=-1, blank=True, null=True)
    small_category = models.CharField(max_length=-1, blank=True, null=True)
    relation_goods = models.JSONField(blank=True, null=True)
    sku = models.IntegerField(blank=True, null=True)
    media_list = models.JSONField(blank=True, null=True)
    brand_color = models.CharField(max_length=-1, blank=True, null=True)
    goods_price_str = models.CharField(max_length=-1, blank=True, null=True)
    discount_price_str = models.CharField(max_length=-1, blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    brand_id = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsProductRelation(models.Model):
    gpr_id = models.BigAutoField(primary_key=True)
    goods_id = models.CharField(max_length=-1, blank=True, null=True)
    product_id = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_product_relation'


class ImageRecognition(models.Model):
    mg_id = models.CharField(primary_key=True, max_length=-1)
    first_scan_id = models.CharField(max_length=-1, blank=True, null=True)
    first_user_id = models.CharField(max_length=-1, blank=True, null=True)
    add_info = models.JSONField(blank=True, null=True)
    like_cnt = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_recognition'


class ScanInfo(models.Model):
    scan_id = models.CharField(primary_key=True, max_length=-1)
    mg_id = models.CharField(max_length=-1, blank=True, null=True)
    img_url = models.CharField(max_length=-1, blank=True, null=True)
    crop_img_url = models.CharField(max_length=-1, blank=True, null=True)
    meta_data = models.JSONField(blank=True, null=True)
    user_id = models.CharField(max_length=-1, blank=True, null=True)
    geohash = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    status_flag = models.SmallIntegerField(blank=True, null=True)
    img_name = models.CharField(max_length=-1, blank=True, null=True)
    enc_geo = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scan_info'


class ScanLike(models.Model):
    sl_id = models.BigAutoField(primary_key=True)
    mg_id = models.CharField(max_length=-1, blank=True, null=True)
    scan_id = models.CharField(max_length=-1, blank=True, null=True)
    user_id = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scan_like'
