# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Block(models.Model):
    block_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)
    blocked_user_id = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block'


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


class Follow(models.Model):
    follow_id = models.BigAutoField(primary_key=True)
    user_id = models.UUIDField()
    target_id = models.UUIDField()
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'follow'


class Report(models.Model):
    report_id = models.BigAutoField(primary_key=True)
    user_id = models.UUIDField()
    reported_user_id = models.UUIDField()
    report_reason = models.CharField(max_length=-1)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report'


class UserTagPool(models.Model):
    user_tag_pool_id = models.BigAutoField(primary_key=True)
    user_tag = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tag_pool'


class Users(models.Model):
    user_id = models.UUIDField(primary_key=True)
    account_id = models.UUIDField()
    email = models.CharField(max_length=-1)
    user_tag = models.CharField(max_length=-1)
    username = models.CharField(max_length=-1, blank=True, null=True)
    profile_img = models.CharField(max_length=-1, blank=True, null=True)
    profile_msg = models.CharField(max_length=-1, blank=True, null=True)
    user_tag_changed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    following_cnt = models.IntegerField()
    follower_cnt = models.IntegerField()
    f4f_cnt = models.IntegerField()
    creator_level = models.IntegerField()
    agree_promotion_terms_at = models.DateTimeField(blank=True, null=True)
    app_version = models.CharField(max_length=-1, blank=True, null=True)
    device_lang = models.CharField(max_length=-1, blank=True, null=True)
    device_type = models.CharField(max_length=-1, blank=True, null=True)
    os_type = models.CharField(max_length=-1, blank=True, null=True)
    os_version = models.CharField(max_length=-1, blank=True, null=True)
    player_id = models.CharField(max_length=-1, blank=True, null=True)
    push_token = models.CharField(max_length=-1, blank=True, null=True)
    udid = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
