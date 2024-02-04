from socket import socket, AF_INET, SOCK_STREAM
# AF_INET 用于Internet之间的进程通信
# SOCK_STREAM 表示的是用TCP协议编程

# 1）创建socket对象
server = socket(AF_INET, SOCK_STREAM)
# 2）绑定IP地址和端口
ip='127.0.0.1' # 等同于local
port=8080 # 端口的范围
server.bind(('127.0.0.1', 8080))

# 3）使用listen()进行监听
server.listen(5)
print('服务器启动成功，等待客户端的连接...')

# 4）等待客户端的链接
client, addr = server.accept() # 系列解包赋值

# 5）接收来自客户端的数据
data = client.recv(1024)
print('客户端发送的数据是：', data.decode('utf-8')) # 要求客户端发送过来的数据是使用utf-8送行编码的

# 6）关闭socket
client.close()