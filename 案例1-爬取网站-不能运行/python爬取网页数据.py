# coding=utf-8
import urllib
import re
# 百度贴吧网址:https://tieba.baidu.com/index.html
url="https://tieba.baidu.com/index.html"
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
        # downloadJPG(url, ''.join(\[path, '{0}.jpg'.format(count)\]))
        # downloadJPG(url, path + '{0}.jpg'.format(count))
        downloadJPG(url, str(path) + '{0}.jpg'.format(count))
        print ("下载图片第:", count, "张")
        count += 1
# 封装:从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)
def main():
    url = "http://www.xiaofamao.com/dongman/"
    download(url)
# if \_\_name\_\_ == '\_\_main\_\_':
if __name__ == '__main__':
    main()