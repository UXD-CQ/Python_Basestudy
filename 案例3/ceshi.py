# 下载所有html文件
import requests
from bs4 import BeautifulSoup
import pprint
import json

# 定义一个函数，用于下载所有html文件
def download_all_htmls():
    # 创建一个空列表，用于存储所有html文件
    htmls=[]
    # 循环10次，用于遍历网页
    for idx in range(10):
        # 定义要访问的网页url
        url=f'http://www.crazyant.net/page/{idx+1}'
        # 打印当前正在爬取的网页
        print('craw html:',url)
        # 使用requests模块的get方法访问网页
        r = requests.get(url)
        # 如果网页访问失败，抛出异常
        if r.status_code != 200:
            raise Exception('error')
        # 将网页内容添加到htmls列表中
        htmls.append(r.text)
    # 返回htmls列表
    return htmls

# 调用download_all_htmls函数，下载所有html文件
htmls = download_all_htmls()
