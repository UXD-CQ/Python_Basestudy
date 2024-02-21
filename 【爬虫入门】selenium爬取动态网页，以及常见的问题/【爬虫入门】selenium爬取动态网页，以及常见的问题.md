- [一、概述](#一概述)
  - [1.什么叫做动态网页](#1什么叫做动态网页)
  - [2.为什么要研究动态网页](#2为什么要研究动态网页)
  - [3.静态网页](#3静态网页)
- [二、为什么要使用selenium](#二为什么要使用selenium)
    - [1.selenium是什么](#1selenium是什么)
    - [2.selenium用于爬虫的优点](#2selenium用于爬虫的优点)
    - [3.selenium用于爬虫的缺点](#3selenium用于爬虫的缺点)
- [三、简单操作selenium的方法，从零开始](#三简单操作selenium的方法从零开始)
    - [1. 安装Google浏览器，以及对应版本的驱动器ChromeDriver，配置环境变量](#1-安装google浏览器以及对应版本的驱动器chromedriver配置环境变量)
    - [2. pip安装selenium](#2-pip安装selenium)
    - [3. 打开和关闭浏览器](#3-打开和关闭浏览器)
    - [4. 获取网址](#4-获取网址)
    - [5. 寻找节点n](#5-寻找节点n)
    - [6. 输入信息](#6-输入信息)
    - [7. 点击按钮](#7-点击按钮)
    - [8. 获取某个子属性，比如href](#8-获取某个子属性比如href)
    - [9. 将browser的指令移到新打开的小窗口处](#9-将browser的指令移到新打开的小窗口处)
    - [10. 将browser的指令移回到旧的小窗口处](#10-将browser的指令移回到旧的小窗口处)
    - [11. 根据正文text内容筛选节点（xpath表达式的知识）](#11-根据正文text内容筛选节点xpath表达式的知识)
    - [12. 寻找并列相邻的下一个节点（xpath表达式的知识）](#12-寻找并列相邻的下一个节点xpath表达式的知识)
    - [13. selenium 谷歌浏览器版本更新报错解决（该方法不可行，请保持正常更新）](#13-selenium-谷歌浏览器版本更新报错解决该方法不可行请保持正常更新)
    - [14. 长时间爬取，自动移动鼠标防止锁屏](#14-长时间爬取自动移动鼠标防止锁屏)
    - [15. 将滑动条拖动到底](#15-将滑动条拖动到底)
    - [16. 更多操作](#16-更多操作)
- [四、selenium爬虫实战1——以LOL数据网站opgg为例](#四selenium爬虫实战1以lol数据网站opgg为例)
  - [1.爬取信息](#1爬取信息)
  - [2.制作成可执行文件](#2制作成可执行文件)
- [五、selenium爬虫实战2——利用鼠标移动操作巧妙爬取highcharts动态图表](#五selenium爬虫实战2利用鼠标移动操作巧妙爬取highcharts动态图表)
  - [1.如何操作鼠标](#1如何操作鼠标)
  - [2.更多操作](#2更多操作)
  - [3.有关移动操作](#3有关移动操作)

# 一、概述
## 1.什么叫做动态网页
## 2.为什么要研究动态网页
因为目前动态网页的数量 > 静态网页的数量
## 3.静态网页
scrapy, beatiful soup, bs4...

# 二、为什么要使用selenium
### 1.selenium是什么
它是一款网页浏览器的模拟器，通常用来做网页测试。
### 2.selenium用于爬虫的优点
- 直观、简单：直接模拟用户行为，用户加载网页获取网页源码
- 与scrapy结合（通过middlewire中间件）
- 多种web-driver（browser）浏览器，交互：phantomjs（无头），chrome
### 3.selenium用于爬虫的缺点
- 易识别
```python
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# 增加无头
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 防止被网站识别
chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])

browser = webdriver.Chrome(chrome_options = chrome_options)
```
- 易崩溃
selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: Unknown Error! (0)
记得及时关闭浏览器，同时不能打开太多浏览器页面

- 不易做成可执行文件 .exe
# 三、简单操作selenium的方法，从零开始
### 1. 安装Google浏览器，以及对应版本的驱动器ChromeDriver，配置环境变量
浏览器搜索ChromeDriver</br>
https://chromedriver.chromium.org/downloads</br>
http://chromedriver.storage.googleapis.com/index.html</br>
配置环境变量

phantomjs</br>
https://phantomjs.org/download.html</br>
phantomjs.exe放到和python.exe同目录下

其他浏览器 Ie Firefox。。。</br>
其他浏览器参见博客：https://blog.csdn.net/lcm_up/article/details/38302143

### 2. pip安装selenium
cmd下运行</br>
pip install selenium(不推荐)</br>
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium</br>
pip install 库包名 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

### 3. 打开和关闭浏览器
```python
browser = selenium.webdriver.Chrome() # 打开谷歌浏览器
browser = selenium.webdriver.PhantomJS('C:\Users\e\PycharmProjects\untitled\venv\Scripts\phantomjs') # 打开PJS浏览器
browser.close() # 关闭当前标签页，如果只有一个则关闭浏览器
browser.quit()  # 彻底关闭，包括后台进程
```
### 4. 获取网址
```python
browser.get("https://www.yuque.com/qiguihongtong/kb/bg93pz/edit")
```
### 5. 寻找节点n
```python
node = browser.find_element_by_xpath("//span[@style = 'user-select: auto;']") # 寻找单节点
nodes = browser.find_elements_by_xpath("//span[@style = 'user-select: auto;']") # 寻找多节点
```
xpath helper</br>
~~找到节点之后，可以通过node.text~~

如果你只想通过selenium爬取静态网页，并且不想学习网页语言： text = browser.page_source 再通过正则表达式
### 6. 输入信息
```python
input = browser.find_element_by_xpath('//input')
input.send_keys('青')
```
### 7. 点击按钮
```python
button = browser.find_element_by_xpath('')
button.click() # 不推荐
browser.execute_script("arguments[0].click();", button)
```
### 8. 获取某个子属性，比如href
```python
btn = browser.find_element_by_xpath(".//div[@class='p-img']//a")
print(btn.get_attribute('href'))
```
### 9. 将browser的指令移到新打开的小窗口处
```python
# time.sleep(0.5) # 如果移转失败，请增大这个时间
windows = browser.window_handles
browser.switch_to.window(windows[-1])
```
### 10. 将browser的指令移回到旧的小窗口处
```python
windows = browser.window_handles
browser.switch_to.window(windows[0])
```
### 11. 根据正文text内容筛选节点（xpath表达式的知识）
```python
submit_btn = browser.find_element_by_xpath("//button[text()='发送提问']")
```
### 12. 寻找并列相邻的下一个节点（xpath表达式的知识）
在后面加上//following-sibling::*[1]，例如：<br>
这种方法可实用用于提取表格的第一个元素（因为表格的text经常是好多个，以这种写法可取第一个）
```python
zongguben = browser.find_element_by_xpath("//dt[text()='总股本：']//following-sibling::*[1]").text
```
### 13. selenium 谷歌浏览器版本更新报错解决（该方法不可行，请保持正常更新）
https://blog.csdn.net/weixin_44318830/article/details/104635665
### 14. 长时间爬取，自动移动鼠标防止锁屏
```python
import pyautogui #这个库需要额外下载
pyautogui.moveTo(600, 700, duration=0.1)
pyautogui.moveTo(650, 750, duration=0.1)
```
### 15. 将滑动条拖动到底
```python
def drop_scroll(browser):
    '''将滑条从头滚动到底,以便让浏览器充分加载'''
    for x in range(1, 11, 2):
        # time.sleep(0.5)
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        browser.execute_script(js)
```
### 16. 更多操作
详见https://www.cnblogs.com/songzhixue/p/11270593.html 非常详细
# 四、selenium爬虫实战1——以LOL数据网站opgg为例
## 1.爬取信息
## 2.制作成可执行文件
# 五、selenium爬虫实战2——利用鼠标移动操作巧妙爬取highcharts动态图表
## 1.如何操作鼠标
```python
from selenium.wevdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
# 进行链式鼠标操作
action =ActionChains(browser)
action.(各种操作1)
action.(各种操作2)
.。。
action(各种操作n)
action.perform
#  进行多次链式操作
action =ActionChains(browser)
action.(各种操作1)
action.(各种操作2)
.。。
action(各种操作n)
action.perform
。。。 # 非鼠标操作
action =ActionChains(browser)
action.(各种操作1)
action.(各种操作2)
.。。
action(各种操作n)
action.perform
```
## 2.更多操作
点击、悬停、拖拽<br>
https://blog.csdn.net/huilan_same/article/details/52305176
## 3.有关移动操作
```python
from selenium.wevdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
# 进行链式鼠标操作
action =ActionChains(browser)
action.move_by_offset(40,50)

action =ActionChains(browser)
action.move_by_offset(10,20)
action.perform()

# x,y = 50,70
action =ActionChains(browser)
action.move_by_offset(10,20)
action.perform()

# x,y = 60,90
```

好用的插件：Page Ruler