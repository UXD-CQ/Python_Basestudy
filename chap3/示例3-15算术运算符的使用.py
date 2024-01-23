# 基础运算
print('加法运算：',2+4)
print('减法运算：',4-2)
print('乘法运算：',4*3)
print('除法运算：',10/2)
print('整除运算：',10//2)
print('取余运算：',10%3)
print('幂运算：',2**3)
# 赋值运算符的使用
x=20
y=10
x=x+y
print('x+y=',x)
x+=y
print('x+=y的结果是：',x)
x*=y
print('x*=y的结果是：',x)
x-=y
print('x-=y的结果是：',x)
x/=y
print('x/=y的结果是：',x) # 数据类型转换为了 浮点数类型
x%=y
print('x%=y的结果是：',x)

z=3
y//=z
print('y//z=z的结果是：',y)

y**=2
print('y**=2的结果是：',y)

a=b=c=100
print('a,b,c=',a,b,c)

a,b=10,20
print('a,b=',a,b)

a,b=b,a
print(a,b)