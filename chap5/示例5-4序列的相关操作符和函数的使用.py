s='helloworld'
print('e在helloworld中存在吗？',('e'in s))
print('v在helloworld中存在吗？',('v'in s))
print('e在helloworld不中存在吗？',('e'not in s))
print('v在helloworld不中存在吗？',('v'not in s))

print('len():',len(s))
print('max():',max(s))
print('min():',min(s))

#序列对象的方法，使用序列的名称，打点调用
print('s.index():',int(s.index('o')+1))
print('s.count():',s.count('l'))