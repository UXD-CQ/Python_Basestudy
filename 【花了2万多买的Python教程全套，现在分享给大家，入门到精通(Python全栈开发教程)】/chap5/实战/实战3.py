#模拟12306火车票订票流程
#创建字典用于存储车票信息，使用车次作key 其他信息作 value
dict_ticket = {
        'G1569': ['北京南-天津南','18:06','18:39','00:33'],
        'G1567': ['北京南-天津南','18:15','18:49','00:34'],
        'G8917': ['北京南-天津西','18:20','19:19','00:59'],
        'G203': ['北京南-天津南','18:35','19:09','00:34']
    }
print('车次\t出发站-到达站\t出发时间\t到达时间\t历时时长')
#遍历字典中的元素
for key in dict_ticket.keys():
    print(key,end=('\t'))
    #根据key获取的值是一个列表
    for item in dict_ticket[key]: #根据key获取值
        print(item,end=('  \t '))
    #换行
    print()

#输入用户的购票车次
choose_ticket = input('请输入您要购票的车次：')
#根据key 获取值
info_ticket = dict_ticket.get(choose_ticket,'车次不存在') #info是一个列表类型
if info_ticket != '车次不存在':
    person=input('请输入乘车人，如果是多位乘车人使用逗号分隔：')
    # 获取车次的出发站-到达站，出发时间
    s=info_ticket[0]+' '+info_ticket[1]+'开'
    print('您已经购买了'+choose_ticket+' '+s,'请'+person+',尽快换区纸质车票。【铁路客服】')
else:
    print('车次不存在')