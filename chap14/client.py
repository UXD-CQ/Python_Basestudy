# coding:utf-8
from socket import socket, AF_INET, SOCK_STREAM
import wx
import threading
class LcqClient(wx.Frame):
    def __init__(self, client_name):
        # 调用父类的初始化方法
        # None 没有父级窗口
        # id 当前窗口的一个编号
        # pos 窗体的打开位置
        # size 窗体的大小 单位-像素 宽*高
        wx.Frame.__init__(self, None, id=1001, title=client_name+'的客户端', pos=wx.DefaultPosition, size=(400, 450))
        # 创建面板对象
        pl=wx.Panel(self)
        # 在面板上放盒子
        box=wx.BoxSizer(wx.VERTICAL) # VERTICAL垂直方向布局
        # 可伸缩网格布局
        grid=wx.FlexGridSizer(wx.HSCROLL) # HSCROLL 水平方向布局

        # 创建两个按钮
        conn_btn=wx.Button(pl, size=(200,40), label='连接服务器')
        dis_conn_btn=wx.Button(pl, size=(200,40), label='断开连接')

        # 把两个按钮放到可伸缩的网格布局
        grid.Add(conn_btn, 1, wx.TOP|wx.LEFT)
        grid.Add(dis_conn_btn, 1, wx.TOP|wx.RIGHT)
        # (可伸缩的网格布局)添加到box中
        box.Add(grid, 1, wx.ALIGN_CENTER)

        # 只读文本框 显示聊天内容
        self.show_text=wx.TextCtrl(pl, size=(400,210), style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.show_text, 1, wx.ALIGN_CENTER)

        # 创建聊天内容文本框
        self.chat_text=wx.TextCtrl(pl, size=(400,120), style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.chat_text, 1, wx.ALIGN_CENTER)

        # 可伸缩的网格布局
        grid2=wx.FlexGridSizer(wx.HSCROLL) # 水平方向布局
        # 创建两个按钮
        reset_btn=wx.Button(pl, size=(200,40), label='重置')
        send_btn=wx.Button(pl, size=(200,40), label='发送')
        grid2.Add(reset_btn, 1, wx.TOP|wx.LEFT)
        grid2.Add(send_btn, 1, wx.TOP|wx.RIGHT)
        box.Add(grid2, 1, wx.ALIGN_CENTER)

        # 将盒子放到面板中
        pl.SetSizer(box)
        '''----------以上代码是界面的绘制----------'''
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,conn_btn)
        # 实例属性的设置
        self.client_name=client_name
        self.isConnected=False # 存储客户端连接服务器的状态,默认为False,没连
        self.client_socket=None # 设置客户端的socket对象为空

    def connect_to_server(self, event):
        print(f'客户端{self.client_name}连接服务器成功')
        # 如果客户端没有连接服务器，则开始连接
        if not self.isConnected: # 等价于 self.isConnected==False
            # TCP 编程的步骤
            server_host_port=('127.0.0.1',8888)
            # 创建socket对象
            self.client_socket=socket(AF_INET, SOCK_STREAM)
            # 发送连接请求
            self.client_socket.connect(server_host_port)
            # 只要连接成功 发送一条数据
            self.client_socket.send(f'{self.client_name}上线了'.encode('utf-8'))
            # 启动一个线程 客户端的线程与服务器端的线程进行会话
            client_thread=threading.Thread(target=self.recv_data)
            # 设置成守护线程 窗体关闭 子线程随即结束
            client_thread.deamon=True
            # 修改一下连接状态
            self.isConnected=True
            # 启动线程
            client_thread.start()

    def recv_data(self):
        # 如果是连接
        while self.isConnected:
            # 接收来自服务器的数据
            data=self.client_socket.recv(1024).decode('utf-8')
            # 显示到只读文本框中
            self.show_text.AppendText('-'*40+'\n'+data+'\n')

if __name__ == '__main__':
    # 初始化app
    app=wx.App()
    # 创建自己的客户端界面对象
    client=LcqClient('python李常卿')
    client.Show() # 可以改成 client=LcqClient('python李常卿').show()

    # 循环刷新显示
    app.MainLoop()