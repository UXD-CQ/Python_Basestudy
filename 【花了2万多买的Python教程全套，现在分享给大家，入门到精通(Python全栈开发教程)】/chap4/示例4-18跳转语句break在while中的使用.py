s=0 #储存累加值
i=1 #初始化变量
while i<11: #条件判断
    #语句块
    s=s+i
    if s>20:
        print('累加和大于20的当前数是：',i)
        break
    i=i+1 #改变变量
print('-'*10,'登录过程','-'*10)
i=0
while i<3:
    name=input('请输入用户名：')
    pwd=input('请输入密码：')
    if name=='admin' and pwd=='123456':
        print('系统正在登录，请稍后！')
        break
    else:
        if i<2:
            print('用户名或密码错误，您还有',2-i,'次机会')
    i+=1
else:
    print('三次机会钧输入错误，登录失败！')