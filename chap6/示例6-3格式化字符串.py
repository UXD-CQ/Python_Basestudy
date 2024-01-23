# 占位符格式化
name='马冬梅'
age=20
score=98.5
print('我叫%s,今年%d岁了，成绩是%.1f'%(name,age,score))

# f-string
print(f'我叫{name},今年{age}岁了，成绩是{score}')

# 使用字符串的format方法
print('我叫{0},今年{1}岁了，成绩是{2}'.format(name,age,score))
print('我叫{2},今年{0}岁了，成绩是{1}'.format(age,score,name))
