from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

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