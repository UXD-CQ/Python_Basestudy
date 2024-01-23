import time
now=time.time()
print(now)

obj=time.localtime() # struct_time 对象
print(obj)

obj2=time.localtime(60)
print(obj2)
print(type(obj2)) # <class 'time.struct_time'>
print('年份：',obj2.tm_year)
print('月份：',obj2.tm_mon)
print('日期：',obj2.tm_mday)
print('时间：',obj2.tm_hour)
print('分钟：',obj2.tm_min)
print('秒数：',obj2.tm_sec)
print('星期：',obj2.tm_wday+1)
print('一年第几天：',obj2.tm_yday)
print('夏令时：',obj2.tm_isdst)
print(time.ctime())

# 日期时间格式化
print(time.strftime('%Y-%m-%d %H:%M:%S',obj)) # str--字符串f->format--time时间
print('%B月份的名称：',time.strftime('%B',time.localtime()))
print('%A星期的名称：',time.strftime('%A',time.localtime()))

# 字符串转成struct_time
print(time.strptime('2019-01-01','%Y-%m-%d'))

time.sleep(20)
print('sleep 20s hello world')