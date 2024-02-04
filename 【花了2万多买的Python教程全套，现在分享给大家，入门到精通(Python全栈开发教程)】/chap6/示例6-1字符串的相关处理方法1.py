#大小写转换
s1 = "Hello, World!"
new_s2 = s1.lower()
print(s1)
print(new_s2)
new_s3 = new_s2.upper()
print(new_s3)

#字符串的分割
e_mail = "aiui_design@163.com"
lst = e_mail.split("@")
print('邮箱名：',lst[0],'邮件服务器域名：',lst[1])

#
print(s1.count('o'))  # o出现的次数

#检索操作
print(s1.find('o'))  # o首次出现的位置
print(s1.find('p'))  # -1就是没有找到

print(s1.index('o'))
# print(s1.index('p'))  ValueError: substring not found

#判断前缀和后缀
print(s1.startswith('H'))
print(s1.startswith('h'))

print('demo.py'.endswith('.py'))  # True
print('demo.txt'.endswith('.txt'))