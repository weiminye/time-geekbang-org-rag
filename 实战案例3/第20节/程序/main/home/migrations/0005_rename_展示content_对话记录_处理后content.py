# Generated by Django 4.2.13 on 2024-07-07 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_对话记录_已结束'),
    ]

    operations = [
        migrations.RenameField(
            model_name='对话记录',
            old_name='展示content',
            new_name='处理后content',
        ),
    ]
