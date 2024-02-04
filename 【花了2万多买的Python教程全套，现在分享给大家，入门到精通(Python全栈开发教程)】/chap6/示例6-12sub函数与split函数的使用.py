import re #导入正则表达式
pattern = '黑客|破解|反爬'
s='我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗'
new_s = re.sub(pattern,'XXX',s) #调用sub函数
print(new_s)

s2='https://www.baidu.com/s?wd=yyds&rsv_spt=1'
pattern2='[?|&]'
new_s2 = re.split(pattern2,s2) #调用split函数
print(new_s2)