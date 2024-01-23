# 编写函数实现操作符in的功能
# 使用input()从键盘获取一个字符串，判断这个字符串在列表中是否存在（函数体不能使用in），返回结果为True或False
def check_in(string, lst):
    if string in lst:
        return True
    else:
        return False

# 测试函数
lst = ['apple', 'banana', 'orange', 'grape']
string = input("请输入一个字符串：")
result = check_in(string, lst)
print('存在' if result else '不存在')