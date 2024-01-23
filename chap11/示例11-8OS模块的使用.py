import os
print('获取当前的工作路径：',os.getcwd(),'\n')
lst=os.listdir()
print('当前工作路径下的文件和文件夹列表：',lst,'\n')
print('当前工作路径下的文件和文件夹数量：',len(lst))
print('指定路径下所有目录及文件：',os.listdir('../../PythonProject'),'\n')

# 创建目录
# os.mkdir('好好学习') # 如果要创建的文件夹存在程序报错FileExistsError
# os.makedirs('./aa/bb/cc')

# 删除目录
# os.rmdir('./好好学习') # FileNotFoundError 如果要删除的目录不存在，程序会报错
# os.removedirs('./aa/bb/cc')

# 改变当前的工作路径
# os.chdir('../../PythonProject')
# print('改变当前的工作路径后的路径：',os.getcwd(),'\n')

# 遍历目录树 相当于递归
for dirs,dirlst,filelst in os.walk('../../PythonProject'):
    print('遍历目录树：',dirs)
    print('遍历目录树：',dirlst)
    print('遍历目录树：',filelst)
    print('----------------------------------------')