#创建字典
d={10:'cat',20:'dog',30:'bird',10:'cat'}
print(d) #key值相同时 value进行了覆盖
#zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','bird','cow']
zipojb=zip(lst1,lst2)
print(zipojb) #<zip object at 0x104c0fb40>
# print(list(zipojb))  [(10, 'cat'), (20, 'dog'), (30, 'bird'), (40, 'cow')]
d=dict(zipojb)
print(d) #{10: 'cat', 20: 'dog', 30: 'bird', 40: 'cow'}
#使用参数创建字典
d=dict(cat=10,dog=20,monkey=30) # 左侧a是键 右侧的是value
print(d)

t=(10,20,30)
print({t:10}) #t是键 10是value 元组是可以作为字典中的key

# lst=[10,20,30]  列表不可以作为字典中的key ↓
# print({lst:10}) TypeError: unhashable type: 'list'

#字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))

#字典是删除
del d
# print(d)