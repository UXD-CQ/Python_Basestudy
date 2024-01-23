user_name=input("请输入用户名：")
pwd=input("请输入密码：")
if user_name=="admin" and pwd=="123456":
    print("登录成功")
else:
    print("用户名或密码错误")