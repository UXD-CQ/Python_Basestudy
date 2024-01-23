s={10,20,30}
# 向集合中添加元素 add
s.add(100)
print(s)
# 删除元素
s.remove(10)
print(s)
# 清空所有元素
s.clear()
print(s)

# 集合的遍历操作
s={10,20,30}
for i in s:
    print(i)

for index,value in enumerate(s):
    print(index,'-->',value) #index-->序号

#集合的生成式
s={i for i in range(1,10)}
print(s)

s={i for i in range(1,10) if i%2==1}
print(s)