from selenium import webdriver
from bs4 import BeautifulSoup

# 创建一个webdriver实例
driver = webdriver.Chrome()

# 打开一个网页
driver.get('https://www.mi.com/')

# 获取网页的HTML内容
html = driver.page_source

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html, 'html.parser')

# 获取所有的HTML元素
elements = soup.find_all()

# 打印所有的HTML元素
for element in elements:
    print(element)
    print('-'*20+'HTML元素完成'+'-'*20)

# 获取网页的CSS样式
css = driver.execute_script("return document.styleSheets")

# 打印所有的CSS样式
for style in css:
    print(style)
    print('-'*20+'css样式完成'+'-'*20)
# 获取网页的JavaScript代码
javascript = driver.execute_script("return document.scripts")

# 打印所有的JavaScript代码
for script in javascript:
    print(script)
    print('-'*20+'JavaScript代码完成'+'-'*20)

# 关闭webdriver实例
driver.quit()
