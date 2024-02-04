import os.path
print('获取目录或文件的绝对路径：',os.path.abspath('./file1.txt'))
print('判断目录或文件在磁盘上是否存在：',os.path.exists('./file1.txt'))
print('拼接路径：',os.path.join('./dir1','file1.txt'))
print('分割文件的名和后缀名：',os.path.splitext('./file1.txt')) # 元组类型
print('提取文件名：',os.path.basename(r'/Users/ued_qing/Documents/PythonProject/chat11/google1.jpg'))
print('提取路径：',os.path.dirname(r'../PythonProject/chat11/google1.jpg'))
print('判断是否是有效路径：',os.path.isdir('../../PythonProject/chat11'))
print('判断是否是有效文件：',os.path.isfile('./file1.txt'))