import re #导入正则表达式
pattern = '\d\.\d+' # +表示1个或多个 \d表示数字 \.表示小数点
s='I study Python 3.12 every day' #待匹配的字符串
match = re.match(pattern,s,re.I) #调用match函数 re.I表示忽略大小写
print(match) # None

s2='3.12 Python I study  every day'
match2 = re.match(pattern,s2,re.I)
print(match2) # <re.Match object; span=(0, 4), match='3.12'>
print('-'*50)
print('匹配值的起始位置：',match2.start())
print('匹配值的结束位置：',match2.end())
print('匹配区间的位置元素：',match2.span())
print('待匹配的字符串：',match2.string)
print('匹配的数据：',match2.group())