# Generated by Django 4.0.4 on 2023-09-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aurora', '0005_summarycontentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryScanDailyInfo',
            fields=[
                ('summary_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('summary_dt', models.CharField(blank=True, max_length=255, verbose_name='통계일자')),
                ('scan_success', models.BigIntegerField(blank=True, default=0, verbose_name='스캔성공')),
                ('scan_fail', models.BigIntegerField(blank=True, default=0, verbose_name='스캔실패')),
                ('total_scan_user', models.BigIntegerField(blank=True, default=0, verbose_name='스캔참여회원')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'summary_scan_daily_info',
            },
        ),
        migrations.CreateModel(
            name='SummaryScanHourInfo',
            fields=[
                ('summary_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('summary_dt', models.CharField(blank=True, max_length=255, verbose_name='통계일자')),
                ('scan_success', models.BigIntegerField(blank=True, default=0, verbose_name='스캔성공')),
                ('scan_fail', models.BigIntegerField(blank=True, default=0, verbose_name='스캔실패')),
                ('total_scan_user', models.BigIntegerField(blank=True, default=0, verbose_name='스캔참여회원')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'summary_scan_hour_info',
            },
        ),
        migrations.CreateModel(
            name='SummaryScanMonthInfo',
            fields=[
                ('summary_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('summary_dt', models.CharField(blank=True, max_length=255, verbose_name='통계일자')),
                ('scan_success', models.BigIntegerField(blank=True, default=0, verbose_name='스캔성공')),
                ('scan_fail', models.BigIntegerField(blank=True, default=0, verbose_name='스캔실패')),
                ('total_scan_user', models.BigIntegerField(blank=True, default=0, verbose_name='스캔참여회원')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'summary_scan_month_info',
            },
        ),
        migrations.CreateModel(
            name='SummaryUserDailyInfo',
            fields=[
                ('summary_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('summary_dt', models.CharField(blank=True, max_length=255, verbose_name='통계일자')),
                ('total_user', models.BigIntegerField(blank=True, default=0)),
                ('new_user', models.BigIntegerField(blank=True, default=0)),
                ('suspended_user', models.BigIntegerField(blank=True, default=0)),
                ('deleted_user', models.BigIntegerField(blank=True, default=0)),
                ('return_user', models.BigIntegerField(blank=True, default=0)),
                ('inactive_user', models.BigIntegerField(blank=True, default=0)),
                ('dau', models.BigIntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'summary_user_daily_info',
            },
        ),
        migrations.CreateModel(
            name='SummaryUserMonthInfo',
            fields=[
                ('summary_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('summary_dt', models.CharField(blank=True, max_length=255, verbose_name='통계일자')),
                ('total_user', models.BigIntegerField(blank=True, default=0)),
                ('new_user', models.BigIntegerField(blank=True, default=0)),
                ('suspended_user', models.BigIntegerField(blank=True, default=0)),
                ('deleted_user', models.BigIntegerField(blank=True, default=0)),
                ('return_user', models.BigIntegerField(blank=True, default=0)),
                ('inactive_user', models.BigIntegerField(blank=True, default=0)),
                ('dau', models.BigIntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'summary_user_month_info',
            },
        ),
        migrations.DeleteModel(
            name='SummaryScanInfo',
        ),
        migrations.DeleteModel(
            name='SummaryUserInfo',
        ),
        migrations.RemoveField(
            model_name='summarycontentinfo',
            name='reg_date',
        ),
        migrations.RemoveField(
            model_name='summarycontentinfo',
            name='user_cnt',
        ),
        migrations.AddField(
            model_name='summarycontentinfo',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='summarycontentinfo',
            name='summary_dt',
            field=models.CharField(blank=True, max_length=255, verbose_name='통계일자'),
        ),
        migrations.AddField(
            model_name='summarycontentinfo',
            name='total_user',
            field=models.BigIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='summarycontentinfo',
            name='content_cnt',
            field=models.BigIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='summarycontentinfo',
            name='content_type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
