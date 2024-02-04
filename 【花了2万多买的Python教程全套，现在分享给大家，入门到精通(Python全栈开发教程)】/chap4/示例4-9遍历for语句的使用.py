for i in 'hello':
    print(i)
#range()函数，Python的内置函数，产生一个(n,m)的整数序列，包含n但不包含m
for i in range(1,11):
    #print(i)
    if i%2 == 0:
        print(i,'是偶数')
#计算1-10之间的累加和
s=0 # 用于储存累加值
for i in range(1,11):
    s=s+i
print('1-10之间的累加和是：',s)
print('-'*10,'100到999之间的水仙花数','-'*10)
# 153=3*3*3+5*5*5+1*1*1
for i in range(100,1000):
    sd=i%10
    tens=i//10%10
    hundreds=i//100
    if i==sd**3+tens**3+hundreds**3:
        print(i)