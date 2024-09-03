from django.contrib import admin

from .models import 对话记录
from .models import CNET新闻

class 对话记录Admin(admin.ModelAdmin):
    ordering = ["created_time"]
    list_display = ['已结束','created_time','不带入大模型对话中','role', 'content', '处理后content','提交给大模型的playload']
    search_fields = ['已结束']
    list_filter = ['已结束']

admin.site.register(对话记录, 对话记录Admin)

class CNET新闻Admin(admin.ModelAdmin):
    ordering = ["新闻发布日期"]
    list_display = ['标题中文翻译','新闻发布日期','url']
    list_filter = ['新闻发布日期']

admin.site.register(CNET新闻, CNET新闻Admin)