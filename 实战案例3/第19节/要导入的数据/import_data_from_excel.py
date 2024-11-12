# 读取当前目录下的data.xlsx文件
import pandas as pd
import requests

data = pd.read_excel('data.xlsx')

# 遍历数据框中的每一行数据
for index, row in data.iterrows():
    body_json = {
        "知识主表id":row['知识主表id'],
        "知识详细表记录id":row['知识详细表记录id'],
        "模块":row['模块'],
        "标题":row['标题'],
        "url":row['url'],
        "文本内容":row['文本内容'],
        "内容在分段中的顺序":row['内容在分段中的顺序'],
    }
    response = requests.post(f"http://127.0.0.1:8000/api/import-data", json=body_json)
    print("已成功导入：" + response.text)
