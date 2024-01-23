def happy_birthday(name='李常卿',age=22):
    print('亲爱的'+name+'小朋友，祝你生日快乐！')
    print(str(age)+'岁 生日快乐！')

# 调用
happy_birthday() # 不用传参
happy_birthday('王晓峰') # 位置传参
happy_birthday(age=33) # 关键字传参,name采用默认值

# happy_birthday(66)

def fun(a,b=20): # a做为位置参数 b默认值参数
    pass

# def fun(a=20,b): # 语法错误 当位置参数和默认值参数同时存在的时候，位置参数在后会被报错
    pass

# 当位置参数和关健字参数同时存在的时候，应该遵循位置参数在前，默认参数在后