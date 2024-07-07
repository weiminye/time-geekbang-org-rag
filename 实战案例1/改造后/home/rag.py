import json
import os

import requests
from django.core import serializers

from .models import 对话记录

def get_access_token():
  ernie_client_id = os.getenv("baiduclientid")
  ernie_client_secret = os.getenv("baiduclientsecret")
  url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ernie_client_id}&client_secret={ernie_client_secret}"
  
  payload = json.dumps("")
  headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  return response.json().get("access_token")

def 对话模式(messages):
  url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-lite-8k?access_token=" + get_access_token()
  
  json_obj = {
      "messages": messages,
  }

  payload = json.dumps(json_obj)
  headers = {
      'Content-Type': 'application/json'
  }
  
  response = requests.request("POST", url, headers=headers, data=payload)
  json_result = json.loads(response.text)
  if "error_code" in json_result:
    return json_result["error_msg"] + "：" + payload
  else:
    处理后结果 = 对AI结果进一步处理(json_result["result"])
  保存对话记录(messages[-1]["role"],messages[-1]["content"],messages[-1]["content"])
  保存对话记录("assistant",json_result["result"],处理后结果)
  return 处理后结果

def 保存对话记录(role,content,处理后content):
  record = 对话记录()
  record.role = role
  record.content = content
  record.处理后content = 处理后content
  record.save()

def 构造解析用户输入并返回结构化数据用的messages(用户输入):
  messages=[
  {"role": "user", "content": f"""
  请根据用户的输入返回json格式结果：

  示例：
  用户：客户北京极客邦有限公司的款项到账了多少？
  系统：
  {{'模块':'销售对账','客户名称':'北京极客邦有限公司'}}

  用户：{用户输入}
  系统：
  """},
  ]
  return messages

def 对AI结果进一步处理(AI结果):
  return AI结果.replace("```json", '').replace("```", '')

def 将查询结果转为字符串(查询结果):
  json_str = serializers.serialize("json", list(查询结果))
  return_str = ""
  data = json.loads(json_str)
  for current in data:
    for key, value in current['fields'].items():
      return_str += f"{key}：{value}\n"
  return return_str
def 构造查询结果用的messages(查询结果,用户输入):
  return [{"role": "user", "content": f"""
  已经从数据库中查询出如下结果：

  {将查询结果转为字符串(查询结果)}

  请根据以上查询结果回答用户的问题：{用户输入}
  """}]

def 构造全部messages(之前的messages,当前messages):
  if 之前的messages is not None and len(之前的messages) > 0:
    适配大模型的messages = []
    for current in 之前的messages:
      if current.不带入大模型对话中 is False:
        适配大模型的messages.append({"role":current.role, "content":current.content})
    return [*适配大模型的messages,*当前messages]
  else:
    return 当前messages