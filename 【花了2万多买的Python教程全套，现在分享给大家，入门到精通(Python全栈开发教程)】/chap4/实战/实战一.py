print('-'*10,'输入一个年份，判断是否是闰年','-'*10)
year=eval(input("请输入年份："))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"是闰年")
else:
    print(year,"是平年")