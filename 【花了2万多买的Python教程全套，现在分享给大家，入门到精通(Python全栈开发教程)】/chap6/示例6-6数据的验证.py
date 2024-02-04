# 判断字符串'123'是否为数字
print('123'.isdigit()) # True
print('一二三'.isdigit()) # False
print('0b1010'.isdigit()) # False
print('ⅠⅡⅢⅣⅤ'.isdigit()) # False
print('-'*50)
# 所有字符都是数字
print('123'.isnumeric()) # True
print('一二三'.isnumeric()) # True
print('0b1010'.isnumeric()) # False
print('ⅠⅡⅢⅣⅤ'.isnumeric()) # True
print('壹贰叁'.isnumeric()) # True
print('-'*50)
# 所有字符都是字母（包含中文字符）
print('hello你好'.isalpha()) # True
print('hello你好123'.isalpha()) # False
print('hello你好一二三'.isalpha()) # True
print('hello你好ⅠⅡⅢⅣⅤ'.isalpha()) # False
print('hello你好壹贰叁'.isalpha()) # True
print('-'*50)
# 所有字符都是数字或字母
print('hello你好'.isalnum()) # True
print('hello你好123'.isalnum()) # True
print('hello你好一二三'.isalnum()) # True
print('hello你好ⅠⅡⅢⅣⅤ'.isalnum()) # True
print('hello你好壹贰叁'.isalnum()) # True
print('-'*50)
# 判断字符的大小写
print('HELLOWORLD'.islower()) # False
print('helloworld'.islower()) # True
print('hello你好'.islower()) # True
print('HELLOWORLD'.isupper()) # True
print('helloworld'.isupper()) # False
print('HELLO你好'.isupper()) # True
print('-'*50)
# 所有字符都是首字母大写
print('Hello'.istitle()) # True
print('HelloWorld'.istitle()) # False
print('Helloworld'.istitle()) # True
print('Hello World'.istitle()) # True
print('Hello world'.istitle()) # False
print('-'*50)
# 判断是否都是空白字符
print('\t'.isspace()) # True
print(' '.isspace()) # True
print('\n'.isspace()) # True
