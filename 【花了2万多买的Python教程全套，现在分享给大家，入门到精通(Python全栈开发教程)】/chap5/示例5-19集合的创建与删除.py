# {}直接创建集合
s={10,20,30,40,50,60,70,80,90,100}
print(s)
# 集合只能储存不可变数据类型
# s={[10,20],[30,40]}  TypeError: unhashable type: 'list'

# 使用set()创建集合
s=set()
print(s,type(s)) #创建了一个空集合，空集合的布尔值是False
s={} # 创建的是集合还是字典呢
print(s,type(s)) # <class 'dict'>

s=set('helloworld')
print(s)

s2=set([10,20,30,40,50,60,70,80,90,100])
print(s2)

s3=set(range(1,10))
print(s3)

#集合属于序列中的一种
print('max:',max(s3))
print('min:',min(s3))
print('len:',len(s3))

print('10在集合中存在吗？',10 in s3)
print('10在集合中不存在吗？',10 not in s3)

#集合的删除
del s3
# print(s3)  NameError: name 's3' is not defined. Did you mean: 's'?