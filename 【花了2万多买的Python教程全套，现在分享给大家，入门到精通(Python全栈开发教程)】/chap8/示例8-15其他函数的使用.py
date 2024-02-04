# format()
print(format(3.14,'20')) # 默认右对齐
print(format('helloworld','20')) # 默认左对齐
print(format('hello','*<20')) # <左对齐，*表示填充符，20显示的宽度
print(format('hello','*>20'))
print(format('hello','*^20'))

print(format(3.1415936,'.2f'))
print(format(20,'b'))
print(format(20,'o'))
print(format(20,'x'))
print(format(20,'X'))
print('-'*50)
print(len('hello'))
print(len([10,20,30]))
print('-'*50)
print(id(10))
print(id('hello'))
print(type(10),type('hello'))

print(eval('10+30'))
print(eval('10>30'))