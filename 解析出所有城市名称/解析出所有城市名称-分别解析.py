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
    tree_data = tree.xpath('//div[@class="bottom"]/ul/li')
    all_city_names = []
    # 解析到热门城市的名称
    for i in tree_data:
        hot_city_name = i.xpath('./a/text()')[0]
        all_city_names.append(hot_city_name)
    # 解析的是全部城市的名称
    city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in city_names_list:
        city_names = li.xpath('./a/text()')[0]
        all_city_names.append(city_names)
    print(all_city_names,len(all_city_names))
    with open('all_city_names.txt', 'w', encoding='utf-8') as fp:
        fp.write(str(all_city_names) + '\n')

