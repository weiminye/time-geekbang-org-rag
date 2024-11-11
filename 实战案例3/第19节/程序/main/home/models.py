from django.db import models
from pgvector.django import VectorField

class 销售入账记录(models.Model):
    id = models.AutoField(primary_key=True)

    客户 = models.CharField(max_length=255)
    客户向量编码 = VectorField(dimensions=1024,null=True,blank=True)
    客户向量编码模型 = models.TextField(default="bge-large-zh-v1.5")
    入账日期 = models.DateTimeField()
    入账金额 = models.TextField(null=True)
    已到账款项 = models.IntegerField(null=True)
    剩余到账款项 = models.IntegerField(null=True)

class 对话记录(models.Model):
    id = models.AutoField(primary_key=True)

    role = models.TextField()
    content = models.TextField(null=True)
    处理后content = models.TextField(null=True)
    提交给大模型的playload = models.TextField(null=True)
    不带入大模型对话中 = models.BooleanField(default=False)
    已结束 = models.BooleanField(default=False)

    created_time = models.DateTimeField(auto_now_add=True)
    lastmodified_time = models.DateTimeField(auto_now=True)

class 知识主表(models.Model):
    id = models.IntegerField(
         primary_key = True,
         editable = False)
    created_time = models.DateTimeField(auto_now_add=True)
    lastmodified_time = models.DateTimeField(auto_now=True)

    标题 = models.TextField()
    url = models.TextField()
    创建时间 = models.DateTimeField(null=True,blank=True)
    作者 = models.TextField(null=True,blank=True)
    权限 = models.TextField(null=True,blank=True)
    向量编码 = VectorField(dimensions=1024,null=True,blank=True)
    向量编码模型 = models.TextField(default="bge-large-zh-v1.5")

class 知识详细表(models.Model):
    id = models.IntegerField(
         primary_key = True,
         editable = False)  
    created_time = models.DateTimeField(auto_now_add=True)
    lastmodified_time = models.DateTimeField(auto_now=True)

    文本内容 = models.TextField()
    向量编码 = VectorField(dimensions=1024,null=True,blank=True)
    向量编码模型 = models.TextField(default="bge-large-zh-v1.5")
    知识主表 = models.OneToOneField(知识主表, on_delete=models.CASCADE)