#初始化变量
i=0
#条件判断
while i<3:
#语句块
    user_name=input("请输入用户名：")
    pwd=input("请输入密码：")
#登录操作 if…else…
    if user_name=="admin" and pwd=="123456":
        print("系统正在登录，请稍后！")
        #需要改变循环变量，目的：退出循环
        i=8 #第三行 判断 i<3,8<3 False 退出while循环 改变变量
    else:
        if i<2:
            print("用户名或密码错误！您还有",2-i,'次机会')
        i+=1 #改变变量
#单分支判断
if i==3: #当用户名或密码输入三次不正确的时候，循环执行结束，i最大值是3
    print("对不起，三次钧输入错误")