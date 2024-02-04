# 导入socket
# from...import...
# import......
import socket
# 1)创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2)绑定主机和IP端口
s.bind(('127.0.0.1', 9999))
# 3)设置监听（最大的连接数量）
s.listen(5)

# 4)接受客户端TCP连接
client_socket, client_addr = s.accept()

# 5)接收客户端发送的数据
data = client_socket.recv(1024).decode('utf-8') # while循环的四个步骤 info是初始化变量
while data!='bye':                              # 条件判断
    if data!='':
        print('客户端发送的数据：', data)
        # 准备发送的数据
        data = input('请输入要发送的数据：')

        # 服务器端回复客户端
        client_socket.send(data.encode('utf-8'))
        if data == 'bye':
            break
        data = client_socket.recv(1024).decode('utf-8') # 改变变量

# 关闭socket对象
client_socket.close()
s.close()