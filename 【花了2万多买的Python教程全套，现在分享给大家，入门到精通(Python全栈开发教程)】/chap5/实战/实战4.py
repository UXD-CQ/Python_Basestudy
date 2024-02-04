#创建一个空集合
empty_set = set()
for i in range(1,6):
    info=input(f'请输入第{i}位好友的姓名和手机号:')
    #添加到集合
    empty_set.add(info)
#遍历集合
for item in empty_set:
    print(item)