# 编写函数实现将字符串中字母的大小写转换
# 使用input()获取一个字符串，编写并传参，将字符串中所有的小写字母转成大写，将大写字母转换成小写字母
def convert_case(input_string):
    # 将字符串中所有的小写字母转成大写字母
    uppercase_string = input_string.upper()
    return uppercase_string

input_string = input("请输入一个字符串：")
print("转换后的字符串为：", convert_case(input_string))