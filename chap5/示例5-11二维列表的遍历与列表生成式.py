#创建二维列表
lst=[
['城市','同比','环比'],
['北京',96.4,93.2],
['上海',94.9,94.4],
['广州',91.8,91.0],
['深圳',92.3,91.1]
]
print(lst)
# 遍历二维列表 使用双层for循环
for row in lst: #行
    for col in row: #列
        print(col,end='\t')
    print() #换行

#列表生成式生成一个4行5列的二维列表
lst2=[[j for j in range(5)]for i in range(4)]
print(lst2)