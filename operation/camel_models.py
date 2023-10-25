# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    account_id = models.UUIDField(primary_key=True)
    password = models.CharField(max_length=-1)
    email = models.CharField(max_length=-1)
    birth = models.CharField(max_length=-1, blank=True, null=True)
    status = models.IntegerField()
    changed_password_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class AuthCheck(models.Model):
    auth_id = models.BigAutoField(primary_key=True)
    auth_info = models.CharField(max_length=-1)
    auth_type = models.CharField(max_length=-1)
    auth_status = models.SmallIntegerField()
    account_id = models.CharField(max_length=-1, blank=True, null=True)
    auth_key = models.CharField(max_length=-1)
    created_at = models.DateTimeField()
    authenticated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_check'


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
