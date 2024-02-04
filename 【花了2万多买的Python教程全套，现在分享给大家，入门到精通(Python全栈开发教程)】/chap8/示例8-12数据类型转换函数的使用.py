print('非空字符串的布尔值：',bool('Hello'))
print('空字符串的布尔值：',bool(''))
print('空列表的布尔值：',bool(list()))
print('空列表的布尔值：',bool([]))
print('空元组的布尔值：',bool(()))
print('空元组的布尔值：',bool(tuple()))
print('空集合的布尔值：',bool(set()))
print('空字典的布尔值：',bool({}))
print('空字典的布尔值：',bool(dict()))
print('-'*50)
print('非0数值型的布尔值：',bool(123))
print('整数0的布尔值：',bool(0))
print('浮点数0.0的布尔值：',bool(0.0))
print('-'*50)
# 将其他类型转换成字符串类型
print('-'*16,'将其他类型转换成字符串类型','-'*16)
lst=[10,20,30]
print(type(lst),lst)
s=str(lst)
print(type(s),s)

print('-'*16,'float和str转换为int','-'*16)
f=123.456
print(type(f),f)
s=int(f)
print(type(s),s)
print(int(90.7)+int('90'))
# 注意事项
# print(int('90.7')) # ValueError: invalid literal for int() with base 10: '90.7'
# print(int('a')) # ValueError: invalid literal for int() with base 10: 'a'

print('-'*16,'int和str转换为float','-'*16)
print(float(123)+float('123.12'))

s='hello'
print(list(s))

seq=range(1,10)
print(tuple(seq))
print(set(seq))
print(list(seq))
