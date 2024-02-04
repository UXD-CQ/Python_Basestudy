import datetime
# 输入 日期的函数
def input_date():
    inputdate = input("请输入日期（格式：20240101）：")
    datestr=inputdate[0:4]+'--'+inputdate[4:6]+'--'+inputdate[6:] # 切片 切出年月日
    # 类型转换
    dt=datetime.datetime.strptime(datestr, '%Y--%m--%d')
    return dt

# 主程序 运行
if __name__ == '__main__':
    date = input_date()
    # 输入间隔的天数
    in_num=eval(input("请输入间隔的天数："))
    date=date+datetime.timedelta(days=in_num)
    print("您推算的日期为：",date)