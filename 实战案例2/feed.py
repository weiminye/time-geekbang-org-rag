# -*- coding: utf-8 -*-
import json
import subprocess

from bs4 import BeautifulSoup
import requests
import feedparser

import time
from datetime import date, datetime

from 新闻 import *
from rag import *

def 获取数据():
    # 定义要抓取的RSS源
    rss源 = "https://www.cnet.com/rss/news/"
    
    #region 使用feedparser解析RSS源
    feed = feedparser.parse(rss源)

    #region 这段代码纯粹是为了确认我们抓取成功，调试用，可以删除
    for entry in feed.entries:
        print(entry.title)  # 打印标题
        print(entry.link)   # 打印链接
        print(entry.description)  # 打印描述
    #endregion

    #endregion

    #region 将feed.entries保存到本地json文件
    with open('feed.json', 'w', encoding='utf-8') as f:
        json.dump(feed.entries, f, ensure_ascii=False, indent=4)
    #endregion
    return feed.entries

def 获取元数据(current):
    元数据实例 = 元数据()
    元数据实例.set_标题(current.title)
    元数据实例.set_作者(current.author)
    元数据实例.set_创建日期(current.published_parsed)
    元数据实例.set_url(current.link)
    return 元数据实例

def 根据元数据过滤新闻(current元数据):
    今天 = date.today()
    今天struct_time格式 = time.struct_time(今天.timetuple())
    return current元数据.创建日期 > 今天struct_time格式

def 抓取新闻内容(url):
    response = requests.get(url)
    response.encoding = 'utf-8' # 指定编码
    soup = BeautifulSoup(response.text, 'html.parser')

    正文 = soup.find('div', {'class': 'c-pageArticle_content'})
    if 正文 is not None and 正文.text is not None:
        return 正文.text
    else:
        return None

def 文本摘要(输入文本):
    return 对话模式(构造文本摘要messages(输入文本))

def 对长文本进行摘要(输入文本):
  if len(输入文本) > 文本划分长度:
    文本list = 输入文本.split('\n')
    文本摘要结果 = ''
    for 当前文本 in 文本list:
      当前文本摘要结果=文本摘要(当前文本)
      文本摘要结果 += 当前文本摘要结果 + '\n'
    return 文本摘要结果
  else:
    return 文本摘要(输入文本)

def 翻译成中文(输入文本):
    return 对话模式(构造英译中messages(输入文本))

def 对长文本进行翻译(输入文本):
  if len(输入文本) > 文本划分长度:
    文本list = 输入文本.split('\n')
    文本翻译结果 = ''
    for 当前文本 in 文本list:
      当前文本翻译结果=翻译成中文(当前文本)
      文本翻译结果 += 当前文本翻译结果 + '\n'
    return 文本翻译结果
  else:
    return 翻译成中文(输入文本)

def 生成每日简报(今天的新闻list:list):
    print("生成每日简报")

    # 获取当前日期和时间
    now = datetime.now()

    # 将其格式化为字符串，例如 "2023-04-05_14-30-00"
    formatted_date = now.strftime("%Y-%m-%d")

    # 使用日期字符串作为文件名
    每日简报文件 = f"{formatted_date}.CNET每日简报.html"

    with open(每日简报文件, 'w', encoding='utf-8') as f:
        f.write("<html><head><title>CNET每日简报</title></head><body>")
        f.write(f"<h1>CNET每日简报-{formatted_date}</h1>")
        f.write("<ul>")
        for current in 今天的新闻list:
            f.write("<li>")
            f.write("<h2>")
            f.write(current.元数据.标题_中文翻译)
            f.write("</h2>")
            f.write("<p>")
            f.write(current.摘要)
            f.write("</p>")
            f.write("</li>")
        f.write("</ul>")
        f.write("</body></html>")

    return 每日简报文件
def 打开每日简报(每日简报文件):
    # 使用默认的应用程序打开HTML文件
    subprocess.run(['start', 每日简报文件], shell=True, check=True)

if __name__ == "__main__":
    新闻列表 = 获取数据()
    print(f'共获取{len(新闻列表)}条新闻')
    今天的新闻list = []
    入库条数上限 = 2 # 出于教学目的设置的上限，你可以设置为0，表示不限制入库条数
    当前入库条数 = 0
    for current in 新闻列表:
        current元数据 = 获取元数据(current)
        if 根据元数据过滤新闻(current元数据):
            今天的新闻 = 新闻()
            今天的新闻.set_元数据(current元数据)
            print('属于今天的新闻，准备处理')
            今天的新闻.set_新闻内容(抓取新闻内容(今天的新闻.元数据.url))
            if 今天的新闻 is not None and 今天的新闻.新闻内容 is not None:
                今天的新闻.set_摘要(对长文本进行摘要(今天的新闻.新闻内容))
                今天的新闻.set_标题_中文翻译(翻译成中文(今天的新闻.元数据.标题))
                今天的新闻.set_新闻内容_中文翻译(对长文本进行翻译(今天的新闻.新闻内容))
                今天的新闻list.append(今天的新闻)
                当前入库条数 += 1
        else:
            print('不是今天的新闻，跳过')

        if 入库条数上限 > 0 and 当前入库条数 > 入库条数上限:
           break
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(今天的新闻list, f, ensure_ascii=False, indent=4, cls=新闻Encoder)
    每日简报文件 = 生成每日简报(今天的新闻list)
    打开每日简报(每日简报文件)

