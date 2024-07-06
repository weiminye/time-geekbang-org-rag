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
