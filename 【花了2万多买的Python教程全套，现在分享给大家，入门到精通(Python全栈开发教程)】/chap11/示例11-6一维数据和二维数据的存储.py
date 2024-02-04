# 存储和读取一维数据
def my_write():
    # 一维数据可以使用列表，元组和集合  不能使用字典
    lst=['张三','李四','王五','赵六','钱七','孙八']
    with open('student.csv','w') as f:
        f.write(','.join(lst)+'\n') # 将列表转为字符串

def my_read():
    with open('student.csv','r') as f:
        s=f.read()
        lst=s.split(',')
        print(lst)


# 存储和读取二维数据
def my_write_table():
    lst=[
        ['姓名','年龄','性别'],
        ['张三','20','男'],
        ['李四','21','女'],
        ['王五','22','男'],
    ]
    with open('table.csv','w',encoding='utf-8') as f:
        for row in lst: # row类型是列表
            line=','.join(row)+'\n'
            f.write(line)

def my_read_table():
    with open('table.csv','r',encoding='utf-8') as f:
        for line in f:
            lst=line.strip().split(',') # strip()去除字符串首尾空格
            print(lst)

if __name__ == '__main__':
    # my_write()
    # my_read()
    # my_write_table()
    my_read_table()