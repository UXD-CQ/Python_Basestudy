print('-'*10,'格式化输出商品的名称和单价','-'*10)
lst=[
    ['01','电风扇','美的','500'],
    ['02','洗衣机','TCL','1000'],
    ['03','微波炉','老板','400'],
]
print('编号\t\t商品名称\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()
print('-'*50)
# 格式化
for item in lst:
    item[0]='0000'+item[0]
    item[3]='￥{:.2f}'.format(float(item[3]))

print('编号\t\t商品名称\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()
