d={'hello':10,'world':20,'python':30}
# 访问字典中的元素
# 使用d['key']的方式访问字典中的元素，其中key是字典中的一个键。如果指定的键不存在，将会抛出KeyError异常。
print(d['hello'])
# d.get(key)
print(d.get('hello'))

# 两者之间是有区别的，如果key不存在，d[Key]会报错 d.get(key)不会报错，会返回None
# print(d['key'])  KeyError: 'key'
print(d.get('key')) # None
print(d.get('key', '不存在'))

#字典的遍历
for item in d.items():
    print(item) #key=value组成的一个元素
# 在使用for循环遍历时,分别获取key,value
for key,value in d.items():
    print(key,'-->',value)