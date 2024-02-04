'''
实战三:记录用户登录日志并查看
需求:创建XX客服管理系统的登录界面,每次登录时,将用户的登录日志写入文件中,并且可以在程序中查看用户的登录日志
'''
import time
def show_info():
    print('输入提示数字,执行相应的操作:0.退出 1.查看登录日志')

# 记录日志
def write_loginfo(username):
    with open('log.txt', 'a', encoding='utf-8') as f:
        s=f'用户名{username},登入时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}'
        f.write(s)
        f.write('\n')

# 读取日志
def read_loginfo():
    with open('log.txt', 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            else:
                print(line)

if __name__ == '__main__':
    # write_loginfo('admin')
    username = input('请输入用户名:')
    pwd = input('请输入密码:')
    if username == 'admin' and pwd == '123456':
        print('登录成功')
        # 将登录信息写入日志文件
        write_loginfo(username)
        # 提示用户操作
        show_info()
        num=int(input('请输入操作数字:'))
        while True:
            if num == 0:
                print('退出程序')
                break
            elif num == 1:
                print('查看登录日志')
                read_loginfo()
                show_info() # 再调一次显示信息
            else:
                print('输入错误,请重新输入')
                show_info()
            num = int(input('请输入操作数字:'))
    else:
        print('用户名或密码错误')