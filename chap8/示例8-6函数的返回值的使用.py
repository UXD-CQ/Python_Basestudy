# 函数的返回值
def calc(a,b):
    # 计算两个数的和
    print(a+b)

# 调用函数
calc(10,20)
# 调用函数，并返回结果
print(calc(1,2))

# 定义一个函数，计算两个数的和
def calc2(a,b):
    # 计算两个数的和
    s=a+b
    # 返回两个数的和
    return s

# 打印分隔符
print('-'*50)

# 调用函数，并返回结果
get_s=calc2(1,2)
print(get_s)

# 调用函数，并返回结果
get_s2=calc2(calc2(1,2),3)
print(get_s2)

# 返回值可以是多个
def get_sum(num):
    s=0
    odd_sum=0
    even_sum=0
    for i in range(1,num+1):
        if i%2!=0:
            odd_sum+=i
        else:
            even_sum+=i
        s+=i
    return s,odd_sum,even_sum
# 调用函数，并返回结果
get_sum_result=get_sum(10)
print(type(get_sum_result))
print(get_sum_result)

# 解包赋值
s,odd_sum,even_sum=get_sum(10)
print(s,odd_sum,even_sum)