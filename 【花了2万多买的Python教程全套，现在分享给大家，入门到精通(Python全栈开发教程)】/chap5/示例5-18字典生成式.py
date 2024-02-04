import random
d={item :random.randint(1,100) for item in range(4)}
print(d)

#创建两个列表
list1 = [1, 2, 3]
list2 = ['王微微','韩慧慧','李丽丽']
d={key:value for key,value in zip(list1,list2)}
print(d)