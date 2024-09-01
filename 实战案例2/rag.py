import json
import os

import requests

#region 跟具体大模型相关的，如果需要修改大模型，可能需要修改这部分函数
文本划分长度 = 1500

def get_access_token():
  ernie_client_id = os.getenv("baiduclientid")
  ernie_client_secret = os.getenv("baiduclientsecret")
  url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ernie_client_id}&client_secret={ernie_client_secret}"
  
  playload = json.dumps("")
  headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=playload)
  return response.json().get("access_token")

def 对话模式(messages):
  url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-lite-8k?access_token=" + get_access_token()
  
  json_obj = {
      "messages": messages,
  }

  playload = json.dumps(json_obj)
  headers = {
      'Content-Type': 'application/json'
  }
  
  response = requests.request("POST", url, headers=headers, data=playload)
  json_result = json.loads(response.text)
  if "error_code" in json_result:
    return json_result["error_msg"] + "：" + playload
  else:
    return json_result["result"]
#endregion

#region 构造messages相关
def 构造文本摘要messages(输入字符串):
  messages=[
  {"role": "user", "content": f"""
  请对以下文本进行摘要：

  {输入字符串}
  """},
  ]
  return messages

def 构造英译中messages(输入字符串):
  messages=[
  {"role": "user", "content": f"""
  请将以下文本翻译成中文：

  {输入字符串}
  """},
  ]
  return messages

#endregion
