import os
# 删除文件
# os.remove("a.txt") #FileNotFoundError 如果删除的文件不存在，程序会报错

# 重命名
# os.rename('./file.txt', './newfile.txt')

# 转换时间的格式
import time 
def date_format(longtime):
    s=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(longtime))
    return s

# 获取文件信息
info=os.stat('./newfile.txt')
print(type(info),info)

print('最近的一次访问时间：',date_format(info.st_atime))
print('文件的创建时间：',date_format(info.st_ctime))
print('文件的最后一次修改时间：',date_format(info.st_mtime))
# 获取文件大小
print('文件大小：',info.st_size,'字节')

# 启动路径下的文件
# os.startfile(r'/System/Applications/Notes.app')
# 启动python解释器
os.startfile(r'/Library/Frameworks/Python.framework/Versions/3.12/Python.app')