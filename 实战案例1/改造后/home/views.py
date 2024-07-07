import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .rag import 对话模式, 构造全部messages, 构造查询结果用的messages, 构造解析用户输入并返回结构化数据用的messages

from .search import 查询

from .models import 对话记录, 销售入账记录

def newtalk(request):
    未结束的对话 = 对话记录.objects.filter(已结束=False)
    for current in 未结束的对话:
        current.已结束 = True
    对话记录.objects.bulk_update(未结束的对话, ['已结束'])
    return redirect(reverse('home:index'))

def index(request):
    if request.method == 'POST':
        用户输入 = request.POST['question']
        record = 对话记录()
        record.role = "user"
        record.content = 用户输入
        record.展示content = 用户输入
        record.save()
        重试总次数 = 1
        当前重试次数 = 0
        查询结果 = None
        while 当前重试次数 <= 重试总次数:
            try:
                结构化数据 = 对话模式(构造解析用户输入并返回结构化数据用的messages(用户输入))
                record = 对话记录()
                record.role = "assistant"
                record.content = 结构化数据
                record.展示content = 结构化数据
                record.不带入大模型对话中 = True
                record.save()

                查询参数 = json.loads(结构化数据)
                查询结果 = 查询(查询参数)
                break
            except:
                当前重试次数 += 1
        if 查询结果 is not None:
            当前messages = 构造查询结果用的messages(查询结果,用户输入)
            之前的messages = 对话记录.objects.filter(已结束=False,不带入大模型对话中 = True).order_by('created_time')
            全部messages = 构造全部messages(之前的messages,当前messages)
            AI根据查询结果的回答 = 对话模式(全部messages)
            record = 对话记录()
            record.role = "assistant"
            record.content = AI根据查询结果的回答
            record.展示content = AI根据查询结果的回答
            record.save()

    conversation_list = 对话记录.objects.filter(已结束=False).order_by('created_time')
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
