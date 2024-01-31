from selenium import webdriver

# 创建一个webdriver实例
driver = webdriver.Chrome()

# 打开一个网页
driver.get('https://mp.weixin.qq.com/s/rcPw52T3fhjSEAIrnReKrw')

# 获取网页的HTML内容
html = driver.page_source

# 将HTML内容保存到一个文件中
with open('weixin.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 等待10s
driver.implicitly_wait(10)

# 关闭webdriver实例
driver.quit()

# 等待10s
driver.implicitly_wait(10)

# 使用浏览器打开保存的HTML文件
import os
os.system('start weixin.html')
