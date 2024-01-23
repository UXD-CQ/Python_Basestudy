# 编写函数实现计算列表中元素的最大值
# 随机产生10个元素，存储到列表中，编写函数获取这个列表中元素的最大值(不能使用内置函数max())
import random

def find_max(lst):
    # 如果列表为空，返回None
    if not lst:
        return None
    # 初始化最大值为列表第一个元素
    max_val = lst[0]
    # 遍历列表中的每一个元素
    for num in lst:
        # 如果当前元素大于最大值，将当前元素赋值给最大值
        if num > max_val:
            max_val = num
    # 返回最大值
    return max_val

# 生成10个随机数
lst = [random.randint(1, 100) for _ in range(10)]
print(lst)
# 调用函数获取最大值
max_val = find_max(lst)
print("最大值是:", max_val)