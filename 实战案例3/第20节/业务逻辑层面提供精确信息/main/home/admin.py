from django.contrib import admin

from .models import 对话记录
from import_export.admin import ImportExportModelAdmin

class 对话记录Admin(ImportExportModelAdmin):
    list_display = ['不带入大模型对话中','role', '处理后content','positive_review','negative_review']
    search_fields = ['positive_review','negative_review']
    list_filter = ['positive_review','negative_review']

admin.site.register(对话记录, 对话记录Admin)
