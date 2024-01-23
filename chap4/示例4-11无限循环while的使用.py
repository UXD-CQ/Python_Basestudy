#（1）初始化变量↓
answer=input('今天用上课吗？y/n')
while answer=='y': #（2）条件判断
    print('好好学习，天天向上！') #（3）语句块
    #（4）改变变量
    answer=input('今天用上课吗？y/n')

#1-100之间的累加和
sum=0 #储存累加值
i=1 #初始化变量
while i<=100: #条件判断
    sum=sum+i #语句块
    i=i+1 #改变变量
print('1-100之间的累加和为：',sum)