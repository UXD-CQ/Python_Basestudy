# 模拟京东购物流程
#创建一个空列表，用于储存入库的商品信息
lst=[]
for i in range(5):
    goods=input('请输入商品的编号和商品的名称进行商品入库，每次只能输入一件商品:')
    lst.append(goods)
#输出所有的商品信息
for i in lst:
    print(i)
# 空列表 存放购物车商品
cart=[]
while True:
    flag=False #代表没有商品的情况
    num=input('请输入要购买的商品编号:')
    #遍历商品列表，查询一下要购买的商品是否存在
    for i in lst:
        if num ==i[0:4]: #切片操作 总商品中切出序号
            flag=True #代表商品已找到
            cart.append(i) #添加到购物车中
            print('商品已添加到购物车')
            break # 退出的是for循环
    if not flag and num !='q': # not flag等价于 flag==Flase
        print('商品不存在')

    if num=='q':
        break # 退出的是while循环
print('-'*50)
print('您购物车里已选择的商品为：',)
cart.reverse()
for i in cart:
    print(i)