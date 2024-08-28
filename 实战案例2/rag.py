import json
import os

import requests

#region 跟具体大模型相关的，如果需要修改大模型，可能需要修改这部分函数
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
def 构造解析用户输入并返回结构化数据用的messages(之前的用户输入,用户输入):
  if 之前的用户输入 is not None and len(之前的用户输入.strip()) > 0:
    用户输入 = 之前的用户输入 + 用户输入
  messages=[
  {"role": "user", "content": f"""
  请根据用户的输入返回json格式结果，除此之外不要返回其他内容。注意，模块部分请按以下选项返回对应序号：
   1. 销售对账
   2. 报价单
   3. 销售订单
   4. 送货单
   5. 退货单
   6. 其他

  示例1：
  用户：客户北京极客邦有限公司的款项到账了多少？
  系统：
  {{'模块':1,'客户名称':'北京极客邦有限公司'}}

  示例2：
  用户：你好
  系统：
  {{'模块':6,'其他数据',None}}

  示例3：
  用户：最近一年你过得如何？
  系统：
  {{'模块':6,'其他数据',None}}

  用户：{用户输入}
  系统：
  """},
  ]
  return messages

def 构造查询结果用的messages(查询结果,用户输入):
  return [{"role": "user", "content": f"""
  您已经知道以下信息：

  {将查询结果转为字符串(查询结果)}

  请根据以上您所知道的信息回答用户的问题，注意，请简单和直接的回答，不要返回其他内容，不要提“根据您所提供的信息”之类的话。
：{用户输入}
  """}]

def 构造全部messages(之前的messages,当前messages):
  if 之前的messages is not None and len(之前的messages) >= 2:
    适配大模型的messages = []
    for current in list(之前的messages)[:-1]: # 使用-1是为了去掉当前messages
      适配大模型的messages.append({"role":current.role, "content":current.content})
    return [*适配大模型的messages,*当前messages]
  else:
    return 当前messages

#endregion
