# 定义一个函数fac，用来计算阶乘
def fac(n):
    # 如果n等于1或者2，返回1
    if n == 1 or n == 2:
        return 1
    # 否则，返回n-1的阶乘加上n-2的阶乘
    else:
        return fac(n-1)+fac(n-2)
    
# 打印出9的阶乘
print(fac(9)) # 第九位上的数字

# 循环计算1到9的阶乘
for i in range(1,10):
    print(fac(i),end='  ')