# Generated by Django 4.2.13 on 2024-10-04 09:19

from django.db import migrations, models
import pgvector.django.vector


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_对话记录_提交给大模型的playload_alter_对话记录_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='销售入账记录',
            name='客户向量编码',
            field=pgvector.django.vector.VectorField(blank=True, dimensions=1024, null=True),
        ),
        migrations.AddField(
            model_name='销售入账记录',
            name='客户向量编码模型',
            field=models.TextField(default='bge-large-zh-v1.5'),
        ),
    ]
