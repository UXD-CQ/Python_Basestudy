from datetime import datetime # 从datetime模块中导入datetime类
dt=datetime.now()
print("当前系统的日期和时间：",dt)

# datetime是一个类，手动创建这个类的对象
dt2=datetime(2024,1,13,20,55,0)
print('dt2的数据类型：',type(dt2)) # dt2的数据类型： <class 'datetime.datetime'>
print("手动创建的日期和时间：",dt2)
print('year',dt2.year,'month',dt2.month,'day')
print(dt2.day,'hour',dt2.hour,'minute',dt2.minute,'second')

# 比较两个datetime类型的对象大小
labor_day=datetime(2024,10,1,20,55,0)
lavor_day2=datetime(2024,5,1,20,55,0)
print('2028年5月1日比2028年10月1日早吗?',labor_day<lavor_day2)

# datetime类型与字符串进行转换
nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y-%m-%d %H:%M:%S')
print('nowdt数据类型：',type(nowdt),nowdt)
print('nowdt_str数据类型：',type(nowdt_str),nowdt_str)

# 字符串转datetime
str_datetime=('2024年8月1日')
dt3=datetime.strptime(str_datetime,'%Y年%m月%d日')
print('str_datetime的数据类型：',type(str_datetime),str_datetime)
print('dt3数据类型：',type(dt3),dt3)
