import admin.my_admin as a # 包名.模块名 admin是包名 my_admin是模块名
a.info()

print('-'*50)
from admin import my_admin as b # from 包名 import模块 as 别名
b.info()

print('-'*50)
from admin.my_admin import info # from 包名.模块名 import 函数/变量等
info()

from admin.my_admin import *
print(name)