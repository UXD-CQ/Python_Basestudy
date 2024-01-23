# 定义一个函数fac，用于计算阶乘 N!=N*(N-1)!.....1!=1
def fac(n):
    # 如果n等于1，则返回1
    if n == 1:
        return 1
    # 否则返回n乘以阶乘函数的值
    else:
        return n * fac(n-1) # 自己调用自己
    
print(fac(5)) # 5!=5*4*3*2*1=120