print('-'*10,'使用嵌套循环输出九九乘法表','-'*10)
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end='\t')
    print()
print('-'*10,'进阶写法','-'*10)
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,i*j),end='\t')
    print()