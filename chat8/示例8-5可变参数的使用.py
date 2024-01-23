# 个数可变的位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)

# 调用
fun('a', 'b', 'c', 10)
fun(1, 2)
fun('a')
fun([11,22,33,44,55]) # 实际上传的是一个参数
# 在调用时，参数前加一颗星，会将列表进行解包
fun(*[1, 2, 3, 4, 5])

# 个数可变的关键字 参数
def fun2(**kwpara):
    print(type(kwpara))
    for key, value in kwpara.items():
        print(key,'-->',value)

# 调用
fun2(name='李常卿',age=22,hight=188) # 关键字参数

d={'name':'李常卿','age':22,'hight':188}
# fun2(d) #TypeError: fun2() takes 0 positional arguments but 1 was given
fun2(**d)
