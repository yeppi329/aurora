# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# hippo
class Brand(models.Model):
    brand_id = models.CharField(primary_key=True, max_length=255)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    brand_image_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "brand"


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
        db_table = "flyway_schema_history"


class Goods(models.Model):
    goods_id = models.CharField(primary_key=True, max_length=255)
    goods_name = models.CharField(max_length=255, blank=True, null=True)
    goods_desc = models.CharField(max_length=255, blank=True, null=True)
    goods_img = models.CharField(max_length=255, blank=True, null=True)
    goods_price = models.IntegerField(blank=True, null=True)
    goods_ref = models.CharField(max_length=255, blank=True, null=True)
    goods_category = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    mg_id = models.CharField(max_length=255, blank=True, null=True)
    discount_price = models.IntegerField(blank=True, null=True)
    discount_flag = models.BooleanField(blank=True, null=True)
    ci_logo = models.CharField(max_length=255, blank=True, null=True)
    middle_category = models.CharField(max_length=255, blank=True, null=True)
    small_category = models.CharField(max_length=255, blank=True, null=True)
    relation_goods = models.JSONField(blank=True, null=True)
    sku = models.IntegerField(blank=True, null=True)
    media_list = models.JSONField(blank=True, null=True)
    brand_color = models.CharField(max_length=255, blank=True, null=True)
    goods_price_str = models.CharField(max_length=255, blank=True, null=True)
    discount_price_str = models.CharField(max_length=255, blank=True, null=True)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    brand_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "goods"


class GoodsProductRelation(models.Model):
    gpr_id = models.BigAutoField(primary_key=True)
    goods_id = models.CharField(max_length=255, blank=True, null=True)
    product_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "goods_product_relation"


class ImageRecognition(models.Model):
    mg_id = models.CharField(primary_key=True, max_length=255)
    first_scan_id = models.CharField(max_length=255, blank=True, null=True)
    first_user_id = models.CharField(max_length=255, blank=True, null=True)
    add_info = models.JSONField(blank=True, null=True)
    like_cnt = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "image_recognition"


class ScanInfo(models.Model):
    scan_id = models.CharField(primary_key=True, max_length=255)
    mg_id = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    crop_img_url = models.CharField(max_length=255, blank=True, null=True)
    meta_data = models.JSONField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    geohash = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    status_flag = models.SmallIntegerField(blank=True, null=True)
    img_name = models.CharField(max_length=255, blank=True, null=True)
    enc_geo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "scan_info"


class ScanLike(models.Model):
    sl_id = models.BigAutoField(primary_key=True)
    mg_id = models.CharField(max_length=255, blank=True, null=True)
    scan_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "scan_like"


# Lama
class Block(models.Model):
    block_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)
    blocked_user_id = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "block"


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
        db_table = "flyway_schema_history"


class Follow(models.Model):
    follow_id = models.BigAutoField(primary_key=True)
    user_id = models.UUIDField()
    target_id = models.UUIDField()
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "follow"


class Report(models.Model):
    report_id = models.BigAutoField(primary_key=True)
    user_id = models.UUIDField()
    reported_user_id = models.UUIDField()
    report_reason = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "report"


class UserTagPool(models.Model):
    user_tag_pool_id = models.BigAutoField(primary_key=True)
    user_tag = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user_tag_pool"


class Users(models.Model):
    user_id = models.UUIDField(primary_key=True)
    account_id = models.UUIDField()
    email = models.CharField(max_length=255)
    user_tag = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    profile_img = models.CharField(max_length=255, blank=True, null=True)
    profile_msg = models.CharField(max_length=255, blank=True, null=True)
    user_tag_changed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    following_cnt = models.IntegerField()
    follower_cnt = models.IntegerField()
    f4f_cnt = models.IntegerField()
    creator_level = models.IntegerField()
    agree_promotion_terms_at = models.DateTimeField(blank=True, null=True)
    app_version = models.CharField(max_length=255, blank=True, null=True)
    device_lang = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    os_type = models.CharField(max_length=255, blank=True, null=True)
    os_version = models.CharField(max_length=255, blank=True, null=True)
    player_id = models.CharField(max_length=255, blank=True, null=True)
    push_token = models.CharField(max_length=255, blank=True, null=True)
    udid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "users"


# pelican
class Arbecon(models.Model):
    resource_id = models.CharField(max_length=255)
    content = models.OneToOneField("Content", models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = "arbecon"


class Content(models.Model):
    content_type = models.CharField(max_length=31)
    content_id = models.CharField(primary_key=True, max_length=36)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    is_enabled = models.BooleanField()
    last_modified_by = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()
    comment_cnt = models.IntegerField(blank=True, null=True)
    like_cnt = models.IntegerField(blank=True, null=True)
    up_cnt = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    mg_id = models.CharField(max_length=255, blank=True, null=True)
    scan_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    visibility_condition = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "content"


class ContentHashtag(models.Model):
    card = models.OneToOneField("Media", models.DO_NOTHING, primary_key=True)
    hashtag = models.ForeignKey("Hashtag", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "content_hashtag"
        unique_together = (("card", "hashtag"),)


class ContentLike(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=255)
    content_id = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = "content_like"


class ContentLikeRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=255)
    content = models.ForeignKey(Content, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "content_like_relation"


class ContentReply(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    is_enabled = models.BooleanField()
    last_modified_by = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()
    like_cnt = models.IntegerField(blank=True, null=True)
    nested_reply_cnt = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    content = models.ForeignKey(Content, models.DO_NOTHING)
    parent_reply = models.ForeignKey("self", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "content_reply"


class ContentReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    content = models.ForeignKey(Content, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    is_enabled = models.BooleanField()
    last_modified_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "content_report"


class ContentTaggingUser(models.Model):
    content_id = models.CharField(max_length=36)
    user_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "content_tagging_user"


class ContentUp(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    content_id = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = "content_up"


class ContentUpRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    content = models.ForeignKey(Content, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "content_up_relation"


class Drawing(models.Model):
    altitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    point = models.TextField(blank=True, null=True)  # This field type is a guess.
    motion_speed = models.SmallIntegerField(blank=True, null=True)
    motion_type = models.CharField(max_length=255, blank=True, null=True)
    resource_url = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)
    gif_url = models.CharField(max_length=255, blank=True, null=True)
    scan_image_url_for_arcut = models.CharField(max_length=255, blank=True, null=True)
    template_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "drawing"


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
        db_table = "flyway_schema_history"


class Hashtag(models.Model):
    hashtag_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    text = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = "hashtag"


class Media(models.Model):
    altitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    point = models.TextField(blank=True, null=True)  # This field type is a guess.
    media_list = models.JSONField(blank=True, null=True)
    skin = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = "media"


class Post(models.Model):
    post_id = models.CharField(primary_key=True, max_length=36)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    is_enabled = models.BooleanField()
    last_modified_by = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()
    like_cnt = models.IntegerField(blank=True, null=True)
    up_cnt = models.IntegerField(blank=True, null=True)
    mg_id = models.CharField(max_length=255, blank=True, null=True)
    scan_id = models.CharField(max_length=255, blank=True, null=True)
    scan_image_url = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "post"


class PostContentRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    content = models.OneToOneField(Content, models.DO_NOTHING)
    post = models.ForeignKey(Post, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "post_content_relation"


class PostLikeRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    post = models.ForeignKey(Post, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "post_like_relation"


class PostReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    is_enabled = models.BooleanField()
    last_modified_by = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()
    reason = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255)
    post = models.ForeignKey(Post, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "post_report"


class PostUpRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    post = models.ForeignKey(Post, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "post_up_relation"


class ReplyLikeRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=255)
    reply = models.ForeignKey(ContentReply, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "reply_like_relation"


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "spatial_ref_sys"


# camel
class Account(models.Model):
    account_id = models.UUIDField(primary_key=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birth = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    changed_password_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "account"


class AuthCheck(models.Model):
    auth_id = models.BigAutoField(primary_key=True)
    auth_info = models.CharField(max_length=255)
    auth_type = models.CharField(max_length=255)
    auth_status = models.SmallIntegerField()
    account_id = models.CharField(max_length=255, blank=True, null=True)
    auth_key = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    authenticated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "auth_check"


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
        db_table = "flyway_schema_history"
