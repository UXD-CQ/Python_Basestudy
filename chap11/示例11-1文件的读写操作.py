# 写入
def my_write():
    # 1）（创建）打开文件
    f = open("test.txt", "w", encoding="utf-8")
    # 2）操作文件
    f.write("伟大的中国梦!")
    # 3）关闭
    f.close()

# 读取
def my_read():
    # 1）（创建）打开文件
    f = open("test.txt", "r", encoding="utf-8")
    # 2）操作文件
    content = f.read()
    print(type(content),content)
    # 3）关闭
    f.close()

# 主程序运行
if __name__ == "__main__":
    # my_write() # 调用函数
    my_read()