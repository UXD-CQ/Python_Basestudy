x=10
y=3
z=x/y
print(z,type(z))

print('float类型转成int类型',int(z))
print('int类型转成float类型',float(x))

print('100'+'200')
print(int('100')+int('200'))
# print(int(18a))
# print(int('3.12'))
# print(float('18a.788'))

# chr()ord()一对
print(ord('杨'))
print(chr(26472))

print('十进制转成十六进制：',hex(26472))
print('十进制转成八进制：',oct(26472))
print('十进制转成二进制：',bin(26472))