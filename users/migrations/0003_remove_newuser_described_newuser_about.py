# Generated by Django 4.0.4 on 2023-09-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_newuser_about_newuser_described'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='described',
        ),
        migrations.AddField(
            model_name='newuser',
            name='about',
            field=models.TextField(blank=True, max_length=500, verbose_name='about'),
        ),
    ]