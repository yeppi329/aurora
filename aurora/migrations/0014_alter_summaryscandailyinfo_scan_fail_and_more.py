# Generated by Django 4.0.4 on 2023-10-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aurora', '0013_delete_summaryuserterminfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summaryscandailyinfo',
            name='scan_fail',
            field=models.BigIntegerField(default=0, verbose_name='스캔실패'),
        ),
        migrations.AlterField(
            model_name='summaryscandailyinfo',
            name='scan_success',
            field=models.BigIntegerField(default=0, verbose_name='스캔성공'),
        ),
        migrations.AlterField(
            model_name='summaryscandailyinfo',
            name='summary_dt',
            field=models.CharField(max_length=255, unique=True, verbose_name='통계일자'),
        ),
        migrations.AlterField(
            model_name='summaryscandailyinfo',
            name='total_scan_user',
            field=models.BigIntegerField(default=0, verbose_name='스캔참여회원'),
        ),
    ]
