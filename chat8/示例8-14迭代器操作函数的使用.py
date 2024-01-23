lst=[54,56,77,4,567,34]
# 排序操作
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print(lst)
print(asc_lst)
print(desc_lst)

# reversed 反向
reversed_lst=reversed(lst)
print(type(reversed_lst)) # <class 'list_reverseiterator'>
print(list(reversed_lst))

# zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zippobj=zip(x,y)
print(type(zippobj)) # <class 'zip'>
# print(list(zippobj))

# enumerate
enum=enumerate(y,start=1)
print(type(enum)) # <class 'enumerate'>
print(tuple(enum))

# all
lst2=[10,20,30,'',50]
print(all(lst2)) # ‘’是空字符串 False
print(all(lst))

# any
print(any(lst2))

# 
print(next(zippobj))
print(next(zippobj))
print(next(zippobj))

def fun(num):
    return num%2==1 # 可能是True，False
filterobj=filter(fun,range(10)) # 将range(10),0-9的整数，都执行一次fun操作
print(list(filterobj)) # [1, 3, 5, 7, 9]

def upper(x):
    return x.upper()

new_lst2=map(upper,['a','b','c','d'])
print(list(new_lst2))