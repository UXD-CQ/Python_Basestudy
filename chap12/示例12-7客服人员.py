from socket import socket, AF_INET, SOCK_STREAM
# 创建socket对象
server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定IP地址和端口
server_socket.bind(('127.0.0.1', 8888))
while True:
    # 接收数据
    recv_data,addr = server_socket.recvfrom(1024)
    print('客户说：',recv_data.decode('utf-8'))
    if recv_data.decode('utf-8') == 'bye':
        break
    # 准备回复对方的数据
    data=input('客服回：')

    # 发送
    recv_data.sendto(data.encode('utf-8'), addr)

# 关闭socket对象
server_socket.close()