from django.db import models

class 销售入账记录(models.Model):
    id = models.IntegerField(
         primary_key = True,
         editable = False)

    客户 = models.CharField(max_length=255)
    入账日期 = models.DateTimeField()
    入账金额 = models.TextField(null=True)
    已到账款项 = models.IntegerField(null=True)
    剩余到账款项 = models.IntegerField(null=True)

class 对话记录(models.Model):
    id = models.IntegerField(
         primary_key = True,
         editable = False)

    role = models.TextField()
    content = models.TextField(null=True)
    处理后content = models.TextField(null=True)
    提交给大模型的playload = models.TextField(null=True)
    不带入大模型对话中 = models.BooleanField(default=False)
    已结束 = models.BooleanField(default=False)

    created_time = models.DateTimeField(auto_now_add=True)
    lastmodified_time = models.DateTimeField(auto_now=True)

class CNET新闻(models.Model):
    id = models.IntegerField(
         primary_key = True,
         editable = False)

    标题 = models.TextField()
    标题中文翻译 = models.TextField(null=True)
    新闻发布日期 = models.DateTimeField(auto_now_add=True)
    url = models.TextField(null=True)
    作者 = models.TextField(null=True)
    权限 = models.TextField(null=True)    
    新闻内容 = models.TextField(default=False)
    摘要 = models.TextField(default=False)
    新闻内容中文翻译 = models.TextField(default=False)

    created_time = models.DateTimeField(auto_now_add=True)
    lastmodified_time = models.DateTimeField(auto_now=True)