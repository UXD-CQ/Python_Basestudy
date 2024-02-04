print('-'*10,'判断车牌归属地','-'*10)
lst=['京A8888','津B6666','鲁A9999'] # 列表
for item in lst: # 遍历列表
    area = item[0:1] # 切片
    print(f'{item}的车牌归属地是{area}')