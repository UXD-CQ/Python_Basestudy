#使用小括号创建元组
t=('hello',[10,20,30],'python','world')
print(t)

#使用内置函数tuple()创建元组
t=tuple(['hello',[10,20,30],'python','world'])
print(t)

t=tuple([10,20,30,40])
print(t)

print('10在元组中是否存在：',(10 in t))
print('10在元组中是不存在：',(10 not in t))
print('最大值：',max(t))
print('最小值：',min(t))
print('len：',len(t))
print('t.count',t.count(10))
print('t.index',t.index(10))

# 如果元组中只有一个元素 都会不能省
t=(10)
print(t,type(t))

t=(10,)
print(t,type(t))

#元组的删除
del(t)
print(t)