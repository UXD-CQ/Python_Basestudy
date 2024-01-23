# 导入jieba分词库
import jieba
# 打开文件，读取文件内容
with open('/Users/ued_qing/Documents/PythonProject/chat10/华为笔记本.txt', 'r', encoding='utf-8') as file:
    s=file.read()
# print(s)
# 分词
lst=jieba.lcut(s)
# print(lst)

# 去重操作
set1=set(lst) # 使用集合实现去重
#
d={} #key:词,value:出现的次数
for i in set1:
    if len(i)>=2:
        d[i]=0

# print(d)
for i in lst:
    if i in d:
        d[i]=d.get(i)+1
# print(d)
new_lst=[]
for i in d:
    new_lst.append([i,d[i]])
# print(new_lst)
# 列表循环
new_lst.sort(key=lambda x:x[1],reverse=True)
print(new_lst[0:11]) # 显示的是前10项

input()