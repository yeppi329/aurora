# Generated by Django 4.0.4 on 2023-09-22 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aurora', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='summaryscaninfo',
            table='summary_scan_info',
        ),
        migrations.AlterModelTable(
            name='summaryuserinfo',
            table='summary_user_info',
        ),
    ]
