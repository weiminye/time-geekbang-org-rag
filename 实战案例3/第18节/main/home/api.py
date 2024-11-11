import json
from django.http import JsonResponse
import requests

from .models import 销售入账记录
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