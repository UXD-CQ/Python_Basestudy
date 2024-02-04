# 如何用python爬取网页数据,python爬取网页详细教程
内容来源：[如何用python爬取网页数据,python爬取网页详细教程](https://blog.csdn.net/xiaoganbuaiuk/article/details/131367015)
## 目录
- [如何用python爬取网页数据,python爬取网页详细教程](#如何用python爬取网页数据python爬取网页详细教程)
  - [目录](#目录)
- [1. 如何用Python爬虫抓取网页内容?](#1-如何用python爬虫抓取网页内容)
  - [爬虫流程](#爬虫流程)
    - [Requests 使用](#requests-使用)
- [2. 怎样用python爬取网页](#2-怎样用python爬取网页)
- [3. 如何用 Python 爬取需要登录的网站](#3-如何用-python-爬取需要登录的网站)
  - [步骤一：研究该网站](#步骤一研究该网站)
    - [打开登录页面](#打开登录页面)
  - [步骤二：执行登录网站](#步骤二执行登录网站)
  - [步骤三：爬取内容](#步骤三爬取内容)
- [4. python爬虫什么教程最好](#4-python爬虫什么教程最好)
- [5. 如何入门 Python 爬虫](#5-如何入门-python-爬虫)
- [6. 如何入门 Python 爬虫](#6-如何入门-python-爬虫)
- [7. python爬取网页内容数据需要打开网页吗](#7-python爬取网页内容数据需要打开网页吗)
- [8. 如何用Python做爬虫](#8-如何用python做爬虫)
  - [1. 首先你要明白爬虫怎样工作。](#1-首先你要明白爬虫怎样工作)
    - [那么在python里怎么实现呢？很简单](#那么在python里怎么实现呢很简单)
  - [2. 效率](#2-效率)
    - [问题出在哪呢？](#问题出在哪呢)
    - [通常的判重做法是怎样呢？](#通常的判重做法是怎样呢)
  - [3. 集群化抓取](#3-集群化抓取)
    - [考虑如何用python实现：](#考虑如何用python实现)
  - [4. 展望及后处理](#4-展望及后处理)

大家好，本文将围绕python怎么爬取网站所有网页展开说明，如何用python爬取网页数据是一个很多人都想弄明白的事情，想搞清楚python如何爬取网页数据需要先了解以下几个事情。

# 1. 如何用Python爬虫抓取网页内容?

## 爬虫流程

**其实把网络爬虫抽象开来看，它无外乎包含如下几个步骤**

1. 模拟请求网页。模拟浏览器，打开目标网站。
2. 获取数据。打开网站之后，就可以自动化的获取我们所需要的网站数据。
3. 保存数据。拿到数据之后，需要持久化到本地文件或者数据库等存储设备中。

那么我们该如何使用 Python 来编写自己的爬虫程序呢？
在这里我要重点介绍一个 **Python 库：Requests**。

### Requests 使用

Requests 库是 Python 中发起 HTTP 请求的库，使用非常方便简单。
模拟发送 HTTP 请求
发送 GET 请求
当我们用浏览器打开豆瓣首页时，其实发送的最原始的请求就是 GET 请求

```python
import requests
res = requests.get(‘’)
print(res)
print(type(res))
> > >
<Response [200]>
<class ‘requests.models.Response’>
```

# 2. 怎样用python爬取网页

```python
# coding=utf-8
import urllib
import re
# 百度贴吧网址:https://tieba.baidu.com/index.html
# 根据URL获取网页HTML内容
def getHtmlContent(url):
    page = urllib.urlopen(url)
    return page.read()
# 从HTML中解析出所有jpg的图片的URL
# 从HTML中jpg格式为<img ... src = "xxx.jpg" width='''>
def getJPGs(html):
    # 解析jpg图片URL的正则表达式
    jpgReg = re.compile(r'<img.+?src="(.+?\\.jpg)"')
    # 解析出jpg的URL列表
    jpgs = re.findall(jpgReg, html)
    return jpgs
# 用图片url下载图片 并保存成制定文件名
def downloadJPG(imgUrl, fileName):
    urllib.urlretrieve(imgUrl, fileName)
# 批量下载图片,默认保存到当前目录下
def batchDownloadJPGs(imgUrls, path='../'):  # path='./'
    # 给图片重命名
    count = 1
    for url in imgUrls:
        downloadJPG(url, ''.join(\[path, '{0}.jpg'.format(count)\]))
        print "下载图片第:", count, "张"
        count += 1
# 封装:从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)
def main():
    url = "http://www.xiaofamao.com/dongman/"
    download(url)
if \_\_name\_\_ == '\_\_main\_\_':
    main()
```

# 3. 如何用 Python 爬取需要登录的网站

最近我必须执行一项从一个需要登录的网站上爬取一些网页的操作。它没有我想象中那么简单，因此我决定为它写一个辅助教程。

在本教程中，python数据处理，我们将从我们的bitbucket账户中爬取一个项目列表。
教程中的代码可以从我的 Github 中找到。

我们将会按照以下步骤进行：
在本教程中，我使用了以下包（可以在 requirements.txt 中找到）：
**requests
lxml**

---

## 步骤一：研究该网站

### 打开登录页面

进入以下页面 “bitbucket.org/account/signin”。你会看到如下图所示的页面（执行注销，以防你已经登录）

仔细研究那些我们需要提取的详细信息，以供登录之用

在这一部分，我们会创建一个字典来保存执行登录的详细信息：

1. 右击 “Username or email” 字段，选择“查看元素”。我们将使用 “name” 属性为 “username” 的输入框的值。“username”将会是 key 值，我们的用户名/电子邮箱就是对应的 value 值（在其他的网站上这些 key 值可能是 “email”，“ user_name”，“ login”，等等）。</br>
2. 右击 “Password” 字段，选择“查看元素”。在脚本中我们需要使用 “name” 属性为 “password” 的输入框的值。“password” 将是字典的 key 值，我们输入的密码将是对应的 value 值（在其他网站key值可能是 “userpassword”，“loginpassword”，“pwd”，等等）。</br>
3. 在源代码页面中，查找一个名为 “csrfmiddlewaretoken” 的隐藏输入标签。“csrfmiddlewaretoken” 将是 key 值，而对应的 value 值将是这个隐藏的输入值（在其他网站上这个 value 值可能是一个名为 “csrftoken”，“ authenticationtoken” 的隐藏输入值）。列如：“Vy00PE3Ra6aISwKBrPn72SFml00IcUV8”。

最后我们将会得到一个类似这样的字典：

```python
payload = {
“username”: “<USER NAME>”,
“password”: “<PASSWORD>”,
“csrfmiddlewaretoken”: “<CSRF_TOKEN>”
}
```
请记住，这是这个网站的一个具体案例。虽然这个登录表单很简单，但其他网站可能需要我们检查浏览器的请求日志，并找到登录步骤中应该使用的相关的 key 值和 value 值。

## 步骤二：执行登录网站

对于这个脚本，我们只需要导入如下内容：

```python
import requests
from lxml import html
```
**首先**，我们要创建 session 对象。这个对象会允许我们保存所有的登录会话请求。
```python
session_requests = requests.session()
```
**第二**，我们要从该网页上提取在登录时所使用的 csrf 标记。在这个例子中，我们使用的是 lxml 和 xpath 来提取，我们也可以使用正则表达式或者其他的一些方法来提取这些数据。

```python
login_url = “n/?next=/”

result = session_requests.get(login_url)

tree = html.fromstring(result.text)

authenticity_token = list(set(tree.xpath(“//input[@name=‘csrfmiddlewaretoken’]/@value”)))[0]
```
**更多关于xpath 和lxml的信息可以在这里找到。**

接下来，我们要执行登录阶段。在这一阶段，我们发送一个 POST 请求给登录的 url。我们使用前面步骤中创建的 payload 作为 data 。也可以为该请求使用一个标题并在该标题中给这个相同的 url 添加一个参照键。
```python
result = session_requests.post(

    login_url,

    data = payload,

    headers = dict(referer=login_url)

)
```
## 步骤三：爬取内容

现在，我们已经登录成功了，我们将从 bitbucket dashboard 页面上执行真正的爬取操作。

```python
url = ‘/overview’

result = session_requests.get(

url,

headers = dict(referer = url)

)
```
为了测试以上内容，我们从 bitbucket dashboard 页面上爬取了项目列表。我们将再次使用 xpath 来查找目标元素，清除新行中的文本和空格并打印出结果。如果一切都运行 OK，输出结果应该是你 bitbucket 账户中的 buckets / project 列表。

```python
tree = html.fromstring(result.content)

bucket_elems = tree.findall(“.//span[@class=‘repo-name’]/”)

bucket_names = [bucket.text_content.replace(“n”, “”).strip() for bucket in bucket_elems]

print bucket_names
```

你也可以通过检查从每个请求返回的状态代码来验证这些请求结果。它不会总是能让你知道登录阶段是否是成功的，但是可以用来作为一个验证指标。

例如：
```python
result.ok # 会告诉我们最后一次请求是否成功

result.status_code # 会返回给我们最后一次请求的状态
```

* 提取登录需要的详细信息
* 执行站点登录
* 爬取所需要的数据

# 4. python爬虫什么教程最好

可以看这个教程：网页链接
此教程 通过三个爬虫案例来使学员认识Scrapy框架、了解Scrapy的架构、熟悉Scrapy各模块。
此教程的大致内容：
1. Scrapy的简介。
   * 主要知识点：Scrapy的架构和运作流程。
2. 搭建开发环境：
   * 主要知识点：Windows及Linux环境下Scrapy的安装。
3. Scrapy Shell以及Scrapy Selectors的使用。
4. 使用Scrapy完成网站信息的爬取。
   * 主要知识点：创建Scrapy项目(scrapy startproject)、定义提取的结构化数据(Item)、编写爬取网站的 Spider 并提取出结构化数据(Item)、编写 Item Pipelines 来存储提取到的Item(即结构化数据)。

# 5. 如何入门 Python 爬虫
现在之所以有这么多的小伙伴热衷于爬虫技术，无外乎是因为爬虫可以帮我们做很多事情，比如搜索引擎、采集数据、广告过滤等，以Python为例，Python爬虫可以用于数据分析，在数据抓取方面发挥巨大的作用。

但是这并不意味着单纯掌握一门Python语言，就对爬虫技术触类旁通，要学习的知识和规范还有喜很多，包括但不仅限于HTML 知识、HTTP/HTTPS 协议的基本知识、正则表达式、数据库知识，常用抓包工具的使用、爬虫框架的使用等。而且涉及到大规模爬虫，还需要了解分布式的概念、消息队列、常用的数据结构和算法、缓存，甚至还包括机器学习的应用，大规模的系统背后都是靠很多技术来支撑的。
零基础如何学爬虫技术？对于迷茫的初学者来说，爬虫技术起步学习阶段，最重要的就是明确学习路径，找准学习方法，唯有如此，在良好的学习习惯督促下，后期的系统学习才会事半功倍，游刃有余。

用Python写爬虫，首先需要会Python，把基础语法搞懂，知道怎么使用函数、类和常用的数据结构如list、dict中的常用方法就算基本入门。作为入门爬虫来说，需要了解 HTTP协议的基本原理，虽然 HTTP 规范用一本书都写不完，但深入的内容可以放以后慢慢去看，理论与实践相结合后期学习才会越来越轻松。关于爬虫学习的具体步骤，我大概罗列了以下几大部分，大家可以参考：

* 网络爬虫基础知识:
    * 爬虫的定义
    * 爬虫的作用
    * Http协议
    * 基本抓包工具(Fiddler)使用

* Python模块实现爬虫：
    * urllib3、requests、lxml、bs4 模块大体作用讲解
    * 使用requests模块 get 方式获取静态页面数据
    * 使用requests模块 post 方式获取静态页面数据
    * 使用requests模块获取 ajax 动态页面数据
    * 使用requests模块模拟登录网站
    * 使用Tesseract进行验证码识别

* Scrapy框架与Scrapy-Redis：
    * Scrapy 爬虫框架大体说明
    * Scrapy spider 类
    * Scrapy item 及 pipeline
    * Scrapy CrawlSpider 类
    * 通过Scrapy-Redis 实现分布式爬虫
* 借助自动化测试工具和浏览器爬取数据：
    * Selenium + PhantomJS 说明及简单实例
    * Selenium + PhantomJS 实现网站登录
    * Selenium + PhantomJS 实现动态页面数据爬取
* 爬虫项目实战：
  * 分布式爬虫+ Elasticsearch 打造搜索引擎

# 6. 如何入门 Python 爬虫
个人觉得：新手学习python爬取网页先用下面4个库就够了：（第4个是实在搞不定用的，当然某些特殊情况它也可能搞不定）
1. 打开网页，下载文件：urllib
2. 解析网页：BeautifulSoup，熟悉JQuery的可以用Pyquery
3. 使用Requests来提交各种类型的请求，支持重定向，cookies等。
4. 使用Selenium，模拟浏览器提交类似用户的操作，处理js动态产生的网页

这几个库有它们各自的功能。配合起来就可以完成爬取各种网页并分析的功能。具体的用法可以查他们的官网手册(上面有链接)。

做事情是要有驱动的，如果你没什么特别想抓取的，新手学习可以从这个闯关网站开始，目前更新到第五关，闯过前四关，你应该就掌握了这些库的基本操作。

实在闯不过去，再到这里看题解吧，第四关会用到并行编程。（串行编程完成第四关会很费时间哦），第四，五关只出了题，还没发布题解。。。

学完这些基础，再去学习**scrapy**这个强大的爬虫框架会更顺些。这里有它的中文介绍。

这是我在知乎的回答，直接转过来有些链接没有生效，可以到这里看原版，

# 7. python爬取网页内容数据需要打开网页吗

Python爬取网页内容需要打开网页，因为打开网页的时候才可以打开相对于的内容，因此需要爬取对应的数据需要进行内容的爬取网页的打开才可以

# 8. 如何用Python做爬虫
## 1. 首先你要明白爬虫怎样工作。

想象你是一只蜘蛛，现在你被放到了互联“网”上。那么，你需要把所有的网页都看一遍。怎么办呢？没问题呀，你就随便从某个地方开始，比如说人民日报的首页，这个叫initial pages，用$表示吧。

在人民日报的首页，你看到那个页面引向的各种链接。于是你很开心地从爬到了“国内新闻”那个页面。太好了，这样你就已经爬完了俩页面（首页和国内新闻）！暂且不用管爬下来的页面怎么处理的，你就想象你把这个页面完完整整抄成了个html放到了你身上。

突然你发现， 在国内新闻这个页面上，有一个链接链回“首页”。作为一只聪明的蜘蛛，你肯定知道你不用爬回去的吧，因为你已经看过了啊。所以，你需要用你的脑子，存下你已经看过的页面地址。这样，每次看到一个可能需要爬的新链接，你就先查查你脑子里是不是已经去过这个页面地址。如果去过，那就别去了。

好的，理论上如果所有的页面可以从initial page达到的话，那么可以证明你一定可以爬完所有的网页。

### 那么在python里怎么实现呢？很简单

```python
import Queue
initial_page = “初始化页”
url_queue = Queue.Queue()
seen = set()
seen.insert(initial_page)
url_queue.put(initial_page)
while(True): #一直进行直到海枯石烂
if url_queue.size()>0:
current_url = url_queue.get() #拿出队例中第一个的url
store(current_url) #把这个url代表的网页存储好
for next_url in extract_urls(current_url): #提取把这个url里链向的url
if next_url not in seen:
seen.put(next_url)
url_queue.put(next_url)
else:
break
```

写得已经很伪代码了。

所有的爬虫的backbone都在这里，下面分析一下为什么爬虫事实上是个非常复杂的东西——搜索引擎公司通常有一整个团队来维护和开发。

## 2. 效率
如果你直接加工一下上面的代码直接运行的话，你需要一整年才能爬下整个豆瓣的内容。更别说Google这样的搜索引擎需要爬下全网的内容了。

### 问题出在哪呢？
需要爬的网页实在太多太多了，而上面的代码太慢太慢了。设想全网有N个网站，那么分析一下判重的复杂度就是N*log(N)，因为所有网页要遍历一次，而每次判重用set的话需要log(N)的复杂度。OK，OK，我知道python的set实现是hash——不过这样还是太慢了，至少内存使用效率不高。

### 通常的判重做法是怎样呢？
`Bloom Filter.` 简单讲它仍然是一种hash的方法，但是它的特点是，它可以使用固定的内存（不随url的数量而增长）以O(1)的效率判定url是否已经在set中。可惜天下没有白吃的午餐，它的唯一问题在于，如果这个url不在set中，BF可以100%确定这个url没有看过。但是如果这个url在set中，它会告诉你：这个url应该已经出现过，不过我有2%的不确定性。注意这里的不确定性在你分配的内存足够大的时候，可以变得很小很少。一个简单的教程:Bloom Filters by Example

注意到这个特点，url如果被看过，那么可能以小概率重复看一看（没关系，多看看不会累死）。但是如果没被看过，一定会被看一下（这个很重要，不然我们就要漏掉一些网页了！）。 [IMPORTANT: 此段有问题，请暂时略过]

好，现在已经接近处理判重最快的方法了。另外一个瓶颈——你只有一台机器。不管你的带宽有多大，只要你的机器下载网页的速度是瓶颈的话，那么你只有加快这个速度。用一台机子不够的话——用很多台吧！当然，我们假设每台机子都已经进了最大的效率——使用多线程（python的话，多进程吧）。

## 3. 集群化抓取

爬取豆瓣的时候，我总共用了100多台机器昼夜不停地运行了一个月。想象如果只用一台机子你就得运行100个月了…

那么，假设你现在有100台机器可以用，怎么用python实现一个分布式的爬取算法呢？
我们把这100台中的99台运算能力较小的机器叫作slave，另外一台较大的机器叫作master，那么回顾上面代码中的url_queue，如果我们能把这个queue放到这台master机器上，所有的slave都可以通过网络跟master联通，每当一个slave完成下载一个网页，就向master请求一个新的网页来抓取。而每次slave新抓到一个网页，就把这个网页上所有的链接送到master的queue里去。同样，bloom filter也放到master上，但是现在master只发送确定没有被访问过的url给slave。Bloom Filter放到master的内存里，而被访问过的url放到运行在master上的Redis里，这样保证所有操作都是O(1)。（至少平摊是O(1)，Redis的访问效率见:LINSERT – Redis)

### 考虑如何用python实现：

在各台slave上装好scrapy，那么各台机子就变成了一台有抓取能力的slave，在master上装好Redis和rq用作分布式队列。

代码于是写成
```python
#slave.py
current_url = request_from_master()
to_send = []
for next_url in extract_urls(current_url):
to_send.append(next_url)
store(current_url);
send_to_master(to_send)
#master.py
distributed_queue = DistributedQueue()
bf = BloomFilter()
initial_pages = “”
while(True):
if request == ‘GET’:
if distributed_queue.size()>0:
send(distributed_queue.get())
else:
break
elif request == ‘POST’:
bf.put(request.url)
```

好的，其实你能想到，有人已经给你写好了你需要的：`darkrho/scrapy-redis · GitHub`

## 4. 展望及后处理
虽然上面用很多“简单”，但是真正要实现一个商业规模可用的爬虫并不是一件容易的事。上面的代码用来爬一个整体的网站几乎没有太大的问题。

但是如果附加上你需要这些后续处理，比如</br>
有效地存储（数据库应该怎样安排）</br>
有效地判重（这里指网页判重，咱可不想把人民日报和抄袭它的大民日报都爬一遍）</br>
有效地信息抽取（比如怎么样抽取出网页上所有的地址抽取出来，“朝阳区奋进路中华道”），搜索引擎通常不需要存储所有的信息，比如图片我存来干嘛…</br>
及时更新（预测这个网页多久会更新一次）</br>
如你所想，这里每一个点都可以供很多研究者十数年的研究。虽然如此，
“路漫漫其修远兮,吾将上下而求索”。</br>
所以，不要问怎么入门，直接上路就好了：）