# import...
import my_info
print(my_info.name)
my_info.info()

import my_info as a
print(a.name)
a.info()
print('_'*50)
# from...import
from my_info import name
print(name)
# info() # NameError: name 'info' is not defined
from my_info import info
info()

print('_'*50)
# 通配符
from my_info import *
print(name)
info()

# 同时导入多个模块
import math, time, sys