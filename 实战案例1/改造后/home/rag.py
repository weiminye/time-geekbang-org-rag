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