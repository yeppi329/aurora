# Generated by Django 4.0.4 on 2023-09-25 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aurora', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryContentInfo',
            fields=[
                ('summary_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('reg_date', models.CharField(max_length=255)),
                ('content_type', models.CharField(max_length=255)),
                ('content_cnt', models.BigIntegerField(default=0)),
                ('user_cnt', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'summary_content_info',
            },
        ),
    ]
