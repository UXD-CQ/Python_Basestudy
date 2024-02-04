# coding:utf-8
import requests
from lxml import etree
# 项目需求：解析出所有的城市名称 https://www.aqistudy.cn/historydata/
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    # 解析到热门城市和所有城市对应的a标签
    # //div[@class="bottom"]/ul/li/a 热门城市a标签的层级关系
    # //div[@class="bottom"]/ul/div[2]/li/a 所有城市a标签的层级关系
    tree_data = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for i in tree_data:
        city_name = i.xpath('./text()')[0]
        all_city_names.append(city_name)
        print(all_city_names,len(all_city_names))
    with open('所有城市名称.txt', 'w', encoding='utf-8') as fp:
        fp.write(str(all_city_names) + '\n')