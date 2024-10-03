from django.urls import path

from . import views,views_api

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("salescheck", views.salescheck, name="salescheck"),
    path("addsalescheck", views.addsalescheck, name="addsalescheck"),
    path("newtalk", views.newtalk, name="newtalk"),

    path("api/new-talk", views_api.开始新的对话api, name="api-new-talk"),
    path("api/get-query-paras", views_api.获取结构化数据查询参数api, name="api-get-query-paras"),
    path("api/answer-without-data", views_api.从数据库查不到相关数据时的操作api, name="api-answer-without-data"),
    path("api/answer-with-data", views_api.根据查询结果回答用户输入api, name="api-answer-with-data"),
    path("api/get-conversation-list", views_api.获取对话记录api, name="api-get-conversation-list"),
]
