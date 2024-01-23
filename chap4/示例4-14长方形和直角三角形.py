#三行四列
print('-'*10,'三行四列','-'*10)
for i in range(1,4): #外层循环控制行数 
    for j in range(1,5): #内层循环控制打印列数
        print('*', end='')
    print() #空的print语句，作用是控制换行

#直角三角形
print('-'*10,'直角三角形','-'*10)
for i in range(1,6): #五行
    # *的个数与行相同,range(1,2),第二行range(1,3)…
    for j in range(1,i+1):
        print('*', end='')
    print()

#倒直角三角形
print('-'*10,'倒三角形','-'*10)
for i in range(1,6): #五行
    for j in range(1,7-i):
        print('*', end='')
    print()

#等腰三角形
print('-'*10,'等腰三角形','-'*10)
for i in range(1,6):
    for j in range(1,6-i):
        print(' ', end='')
    for k in range(1,i*2):
        print('*', end='')
    print()

#菱形
print('-'*10,'菱形','-'*10)
row=eval(input("请输入菱形的行数："))
while row%2==0:
    row=eval(input("请输入奇数："))
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print('',end=' ')
    for k in range(1,2*bottom_row-2*i+2):
        print('*',end='')
    print()

#空心菱形
print('-'*10,'等#空心菱形','-'*10)
row=eval(input("请输入菱形的行数："))
while row%2==0:
    row=eval(input("请输入奇数："))
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print('',end=' ')
    for k in range(1,2*bottom_row-2*i+2):
        if k==1 or k==2*bottom_row-2*i+2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#三行四列
print('-'*10,'矩形阵列','-'*10)
row=eval(input('请输入行数：'))
while row%2==0:
    row=eval(input('请输入奇数：'))
row_lie=eval(input('请输入列数：'))
for i in range(1,row+1): #外层循环控制行数 
    for j in range(1,row_lie+1): #内层循环控制打印列数
        print('*', end='')
    print() #空的print语句，作用是控制换行

#直角三角形
print('-'*10,'直角三角形','-'*10)
row=eval(input('请输入行数：'))
while row%2==0:
    row=eval(input('请输入奇数行数：'))
for i in range(1,row+1): 
    # *的个数与行相同,range(1,2),第二行range(1,3)…
    for j in range(1,i+1):
        print('*', end='')
    print()

#倒直角三角形
print('-'*10,'倒三角形','-'*10)
row=eval(input('请输入行数：'))
while row%2==0:
    row=eval(input('请输入奇数行数：'))
for i in range(1,row+1): #五行
    for j in range(1,row+2-i):
        print('*', end='')
    print()

#等腰三角形
print('-'*10,'等腰三角形','-'*10)
row=eval(input('请输入行数：'))
while row%2==0:
    row=eval(input('请输入奇数行数：'))
for i in range(1,row+1):
    for j in range(1,row+1-i):
        print(' ', end='')
    for k in range(1,i*2):
        print('*', end='')
    print()
