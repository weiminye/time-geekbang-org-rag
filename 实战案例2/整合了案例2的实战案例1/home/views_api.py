from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import CNET新闻

from .rag import *
def 开始新的对话api(request):
    开始新的对话()
    return JsonResponse({"code":200,"message":"已经成功开始新的对话"})

@csrf_exempt
def 获取结构化数据查询参数api(request):
    用户输入 = request.POST['question']

    查询参数 = 获取结构化数据查询参数(用户输入)
    return JsonResponse({"querydata":查询参数})

def 从数据库查不到相关数据时的操作api(request):
    从数据库查不到相关数据时的操作()
    return JsonResponse({"code":200,"message":"已经成功执行从数据库查不到相关数据时的操作"})

@csrf_exempt
def 根据查询结果回答用户输入api(request):
    用户输入 = request.POST['question']
    查询结果 = request.POST['query-result']

    根据查询结果回答用户输入(查询结果,用户输入)
    return JsonResponse({"code":200,"message":"已经成功根据查询结果回答用户输入"})

def 获取对话记录api(request):
    conversation_list = 获取当前对话记录()
    conversation_list_json = serializers.serialize("json", list(conversation_list))
    return JsonResponse({"conversationlist":conversation_list_json})

@csrf_exempt
def CNET新闻入库api(request):
    # 读取request的json数据
    json_str = request.body.decode("utf-8")
    json_obj = json.loads(json_str)

    # 遍历json数据，将数据写入数据库
    for item in json_obj:
        CNET新闻实例 = CNET新闻()
        CNET新闻.标题 = item.元数据.标题
        CNET新闻.标题中文翻译 = item.元数据.标题_中文翻译
        CNET新闻.新闻发布日期 = item.元数据.创建日期
        CNET新闻.url = item.元数据.url
        CNET新闻.作者 = item.元数据.作者
        CNET新闻.权限 = "CNETNews"
        CNET新闻.新闻内容 = item.新闻内容
        CNET新闻.摘要 = item.摘要
        CNET新闻.新闻内容中文翻译 = item.新闻内容_中文翻译
        CNET新闻实例.save()

    return JsonResponse({"code":200,"message":"已经成功将CNET新闻入库"},
                        json_dumps_params={'ensure_ascii': False})