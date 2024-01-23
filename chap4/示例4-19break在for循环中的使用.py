for i in 'hello':
    if i == 'l':
        break
    print(i)
print('-'*10)
for i in range(3):
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