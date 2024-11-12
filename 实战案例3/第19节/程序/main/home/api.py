import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

from .models import 知识主表, 知识详细表, 销售入账记录
def 调用向量编码服务(输入字符串):
    body_json = {
        "input":输入字符串
    }
    response = requests.post(f"http://127.0.0.1:8902/api/embedding/encode", json=body_json)
    if response.status_code == 200:
        return json.loads(response.text)['向量编码']
    else:
        raise Exception('失败')

def 对知识批量进行向量编码(request):
    未编码的知识list = 销售入账记录.objects.filter(客户向量编码__isnull=True)
    for current in 未编码的知识list:
        current.客户向量编码= 调用向量编码服务(current.客户)
        current.save()
    
    result = {'code':200}
    return JsonResponse(result)

@csrf_exempt
def 导入数据(request):
    if request.method == "POST":
        raw_data = request.body.decode("utf-8")
        json_dict = json.loads(raw_data)

        知识主表记录 = 知识主表()
        知识主表记录.id = json_dict["知识主表id"]
        知识主表记录.模块 = json_dict["模块"]
        知识主表记录.标题 = json_dict["标题"]
        知识主表记录.url = json_dict["url"]
        知识主表记录.向量编码 = 调用向量编码服务(知识主表记录.标题)
        知识主表记录.save()

        知识详细表记录 = 知识详细表()
        知识详细表记录.id = json_dict["知识详细表记录id"]
        知识详细表记录.文本内容 = json_dict["文本内容"]
        知识详细表记录.内容在分段中的顺序 = json_dict["内容在分段中的顺序"]
        知识详细表记录.向量编码 = 调用向量编码服务(知识详细表记录.文本内容)
        知识详细表记录.知识主表 = 知识主表记录
        知识详细表记录.save()

        result = {'文本内容':json_dict["文本内容"]}
        return JsonResponse(result,json_dumps_params={'ensure_ascii': False})