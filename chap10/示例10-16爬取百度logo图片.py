import requests
# 定义一个url
url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'

# 发送请求
resp=requests.get(url)

# 保存到本地
# 打开文件
with open('logo.png','wb') as f:
    # 写入文件
    f.write(resp.content)