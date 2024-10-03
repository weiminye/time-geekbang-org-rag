import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .rag import *

from .search import 查询

from .models import 对话记录, 销售入账记录

from django.core import serializers

def newtalk(request):
    开始新的对话()
    return redirect(reverse('home:index'))

def index(request):
    if request.method == 'POST':
        用户输入 = request.POST['question']

        查询参数 = 获取结构化数据查询参数(用户输入)
        查询结果 = None
        if 查询参数 is not None:
            查询结果 = 查询(查询参数)
            print(f'查询结果={json.dumps(查询结果)}')

        if 查询结果 is None:
            从数据库查不到相关数据时的操作()
        else:
            查询结果json格式 = serializers.serialize("json", list(查询结果))
            根据查询结果回答用户输入(查询结果json格式,用户输入)

    conversation_list = 获取当前对话记录()
    return render(request, "home/index.html",{"object_list":conversation_list})

def salescheck(request):
    # return HttpResponse("home index")
    if request.method == 'POST':
        客户 = request.POST['name']
        if 客户 is not None or 客户.strip() != '':
            object_list = 查询({'模块':'销售对账','客户名称':客户})
        else:
            object_list = 销售入账记录.objects.all()
    else:
        object_list = 销售入账记录.objects.all()

    return render(request, "home/salescheck.html",context={"object_list":object_list})

def addsalescheck(request):
    if request.method == 'POST':
        record = 销售入账记录()
        record.客户 = request.POST['name']
        record.入账日期 = request.POST['created_at']
        record.入账金额 = request.POST['amount']
        record.已到账款项 = request.POST['total']
        record.剩余到账款项 = request.POST['leave']

        record.save()
        return redirect(reverse('home:salescheck'))
    else:
        return render(request, "home/addsalescheck.html")
