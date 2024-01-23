import re #导入正则表达式
pattern = '\d\.\d+' # +表示1个或多个 \d表示数字 \.表示小数点
s='I study Python 3.12 every day python 2.7 I love you' #待匹配的字符串
match = re.findall(pattern,s) #调用findall函数
print(match) # ['3.12', '2.7']