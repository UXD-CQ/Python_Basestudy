print('-'*10,'统计字符串中出现指定字符的次数','-'*10)
s='HelloPython,HelloJava,hellophp'
word=input('请输入要统计的字符：')
print('{0}在{1}一共出现{2}'.format(word,s,s.upper().count(word)))
