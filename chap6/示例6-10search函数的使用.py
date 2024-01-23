import re #导入正则表达式
pattern = '\d\.\d+' # +表示1个或多个 \d表示数字 \.表示小数点
s='I study Python 3.12 every day python 2.7 I love you' #待匹配的字符串
match = re.search(pattern,s) #调用search函数
print(match) # <re.Match object; span=(15, 19), match='3.12'>

s2='4.10 Python I study  every day'
match2 = re.search(pattern,s2)
print(match2) # <re.Match object; span=(0, 4), match='4.10'>

print(match.group())
print(match2.group())