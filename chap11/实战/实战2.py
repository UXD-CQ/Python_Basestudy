'''
实战二:批量创建文件夹
需求:在指定路径newdir下批量创建指定个数的目录(文件夹),如果newdir目录不存在,则创建
'''
import os
import os.path
def mkdirs(path, num):
    for i in range(1,num+1):
        os.mkdir(path+'/'+str(i))

if __name__ == '__main__':
    path='./newdir'
    if not os.path.exists(path):
        os.mkdir(path)
    num=int(input('请输入要创建的文件夹个数:'))
    mkdirs(path,num)