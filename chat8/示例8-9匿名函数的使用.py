def calc(a, b):
    return a + b
print(calc(2, 3))

# 匿名函数
s = lambda a, b: a + b # s 就是一个匿名函数
print(type(s))  # <class 'function'>
# 调用匿名函数
print(s(2, 3))
print('-'*50)

# 列表的正常取值操作
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])
print()

# 使用匿名函数取值
for i in range(len(lst)):
    result = lambda x:x[i] # 根据索引取值，result的类型是function x是形式参数
    print(result(lst)) # lst是实际参数

#
student_score=[
    {'name':'李常卿','score':99},
    {'name':'张三','score':55},
    {'name':'李四','score':100},
    {'name':'王五','score':60}
]
# 对列表进行排序 排序的规则 是字典只是成绩
student_score.sort(key=lambda x:x.get('score'),reverse=True) # 降序
print(student_score)