from datetime import datetime
from datetime import timedelta
# 创建两个datetime类型的对象
delta1 = datetime(2021, 10, 1)-datetime(2021, 1, 1)
print('数据类型：',type(delta1),delta1)
print('2021年1月1日之后的273天是-->',datetime(2021,1,1)+delta1)

# 通过传入参数的方式创建一个timedelta对象
td1=timedelta(10)
print('创建一个10天的timedelta的对象：',td1)
td2=timedelta(10,5)
print('创建一个10天5秒的timedelta的对象：',td2)