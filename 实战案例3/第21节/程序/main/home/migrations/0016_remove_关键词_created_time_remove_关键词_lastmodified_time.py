# Generated by Django 4.2.13 on 2024-11-25 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_关键词'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='关键词',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='关键词',
            name='lastmodified_time',
        ),
    ]
