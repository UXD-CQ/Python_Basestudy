s='hello world'
# 字符串替换
new_s=s.replace('world','世界')
print(new_s)

print(s.center(20))
print(s.center(20,'*'))

#去掉字符串左右的空格
s='  hello   world  '
print(s.strip())  #去掉字符串左右的空格
print(s.lstrip()) #去除字符串左侧的空格
print(s.rstrip()) #去除字符串右侧的空格

# 去掉指定的字符
s='dl-hello world'
print(s.strip('dl'))  # 与顺序无关
print(s.lstrip('dl'))
print(s.rstrip('ld'))
