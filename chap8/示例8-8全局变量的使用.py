a=100 # 全局变量

def fun1(x,y):
    return a+x+y
print(a)
print(fun1(1,2))
print('-'*50)

def fun2(x,y):
    a=200
    return a+x+y
print(a)
print(fun2(1,2))
print('-'*50)

def fun3(x,y):
    global s # s 是全局变量  global
    s=200
    return s+x+y
print(fun3(1,2))
print(s)