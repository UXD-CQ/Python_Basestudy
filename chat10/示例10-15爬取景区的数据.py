# 导入requests模块
import requests
import re
# 设置爬虫打开的浏览器上的网页
url='http://www.weather.com.cn/weather1d/101010100.shtml'
# 使用requests模块的get方法获取网页 打开浏览器并打开网址
resp=requests.get(url)
# 设置编码格式
resp.encoding='utf-8'
print(resp.text) # resp响应对象，对象名.属性名 resp.text

# 使用正则表达式查找城市名
city=re.findall('<span class="name">([/u4e00-\u9fa5]*)</span>',resp.text)
# 使用正则表达式查找天气
weather=re.findall('<span class="weather">([/u4e00-\u9fa5]*)</span>',resp.text)
# 使用正则表达式查找风向
wd=re.findall('<span class="wd">(.*)</span>',resp.text)
# 使用正则表达式查找风力
zs=re.findall('<span class="zs">([/u4e00-\u9fa5]*)</span>',resp.text)
# print(city)
# print(weather)
# print(wd)
# print(zs)

# 创建一个列表
lst=[]
# 使用zip函数将城市名、天气、风向和风力放入列表中
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])
# 遍历列表
for i in lst:
    # 打印列表中的元素
    print(i)