from django.contrib import admin

from .models import 对话记录

class 对话记录Admin(admin.ModelAdmin):
    ordering = ["created_time"]
    list_display = ['已结束','created_time','不带入大模型对话中','role', 'content', '处理后content','提交给大模型的playload']
    search_fields = ['已结束']
    list_filter = ('已结束',)

admin.site.register(对话记录, 对话记录Admin)
