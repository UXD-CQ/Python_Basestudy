#正向递增
s='helloworld'
for i in range(len(s)):
    print(i,s[i],end='  ')
print('\n','-'*10)
#反向递减
for i in range(-10,0):
    print(i,s[i],end=' ')
print('\n',s[9],s[-1])