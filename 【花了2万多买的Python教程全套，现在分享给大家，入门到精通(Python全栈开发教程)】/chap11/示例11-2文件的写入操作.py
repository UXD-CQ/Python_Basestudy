def my_write(s):
    # 1)打开(创建)文件
    file=open('my_write.txt','w')
    # 2)写入内容
    file.write(s)
    file.write('\n')
    # 3)关闭
    file.close()

    #
def my_write_lst(file,lst):
    # 1)打开文件
    f=open(file,'a',encoding='utf-8')    
    # 2)操作文件
    f.writelines(lst)
    # 3)关闭
    f.close()        

# 主程序运行
if __name__ == '__main__':
    # my_write('伟大的中国梦')
    # my_write('北京欢迎您')
    # 准备数据
    lst=['姓名\t','年龄\t','成绩\n','张三\t','30\t','80']
    my_write_lst('my_write.txt',lst)