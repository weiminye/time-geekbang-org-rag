import json
import requests

if __name__ == "__main__":
    # 读取result.json文件,
    with open("result.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    url = "http://127.0.0.1:8000/api/add-cnet-news"
    # 将data做为form-data以post形式发给url
    headers = {'Content-Type': "application/json"}
    response = requests.post(url, json=data,headers=headers)
    
    # 打印response的结果
    print(response.text)
