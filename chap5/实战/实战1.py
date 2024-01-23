lst=[88,89,90,98,00,99] #表示的员工的两位整数出生年份
print('原列表',lst)
# #遍历列表的方式
# for i in range(len(lst)):
#     if str(lst[i]) !='0':
#         lst[i]='19'+str(lst[i]) #拼接年份，再赋值
#     else:
#         lst[i]='200'+str(lst[i])
# print(lst)

for index,value in enumerate(lst):
    if str(value)!='0':
        lst[index]='19'+str(value)
    else:
        lst[index]='200'+str(value)
print(lst)