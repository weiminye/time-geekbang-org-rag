import json
import os

import requests

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
  处理后结果 = 对AI结果进一步处理(json_result["result"])
  return 处理后结果

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