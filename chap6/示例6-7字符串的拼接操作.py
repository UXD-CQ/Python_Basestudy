s1='hello'
s2='world'
# 使用+进行拼接
print(s1+' '+s2)
# 使用字符串的join方法
print(' '.join([s1,s2]))
# 直接拼接
print('hello''world')
# 使用格式化字符串进行拼接
print('%s %s'%(s1,s2))
# 使用f格式化字符串进行拼接
print(f'{s1} {s2}')
# 使用字符串的format方法
print('{} {}'.format(s1,s2))