lst=['hello','world',98,123.5]
print(lst)

lst2=list('helloworld')
lst3=list(range(1,10,2))
print(lst2)
print(lst3)

#列表是序列中的一种，对序列的运作符，运算符，函数均可以使用
print(lst+lst2+lst3)
print(lst*3)
print(len(lst))
print(max(lst3))
print(min(lst3))

print(lst2.count('l'))
print(lst2.index('l'))

lst4=[10,20,30,40,50]
print(lst4)
del lst4[1]
print(lst4)