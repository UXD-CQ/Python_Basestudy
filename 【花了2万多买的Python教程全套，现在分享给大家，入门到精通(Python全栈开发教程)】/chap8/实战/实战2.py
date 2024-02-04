# 编写函数实现提取指定字符串中的数字并求和
# 使用input()获取一个字符串，编写并传参，使用isdigit()方法提取字符串中所有的数字，并对提取的数字进行求和计算，最后将存储数字的列表和累加和返回
def extract_and_sum_numbers(input_string):
    # 提取数字
    numbers = [char for char in input_string if char.isdigit()]
    # 求和
    total = sum(int(num) for num in numbers)
    return numbers, total

# 测试函数
input_str = input("请输入一个字符串：")
numbers, total = extract_and_sum_numbers(input_str)
print("提取的数字列表：", numbers)
print("数字求和结果：", total)