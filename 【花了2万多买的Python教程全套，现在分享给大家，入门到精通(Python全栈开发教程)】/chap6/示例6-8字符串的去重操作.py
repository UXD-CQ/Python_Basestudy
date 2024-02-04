s='helloworldfullwhiceblack'
# 字符串拼接及not in
new_s=''
for i in s:
    if i not in new_s:
        new_s+=i # 字符串拼接操作
print(new_s)

# 使用索引+not in
new_s2=''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2+=s[i]
print(new_s2)

# 使用集合去重+列表的排序操作
new_s3=set(s)
lst=list(new_s3)
lst.sort(key=s.index)
print(''.join(lst))