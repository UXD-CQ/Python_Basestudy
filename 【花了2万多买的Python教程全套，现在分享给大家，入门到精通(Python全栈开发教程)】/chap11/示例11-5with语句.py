def write_fun():
    with open('file.txt', 'w') as f:
        f.write('我是李常卿，我在北京等你！')

def read_fun():
    with open('file.txt', 'r') as f:
        print(f.read())

# 第三个函数
def copy(src_f,target_f):
    with open(src_f, 'r', encoding='UTF-8') as f:
        with open(target_f, 'w', encoding='UTF-8') as f1:
            f1.write(f.read()) # 将读取的内容直接写进文件

if __name__ == '__main__':
    write_fun()
    read_fun()
    # 文件复制
    copy('./file.txt','./file1.txt')