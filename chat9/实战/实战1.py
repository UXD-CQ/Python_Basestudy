# 定义一个圆的类计算面积和周长
import math
class Circle:
    def __init__(self, r):
        self.r = r
    # 计算面积的方法
    def area(self):
        return math.pi * self.r ** 2
    # 计算周长的方法
    def perimeter(self):
        return 2 * math.pi * self.r

# 创建一个圆对象
r=eval(input("请输入圆的半径："))
circle = Circle(r)

# 计算面积和周长
print("圆的面积为:", circle.area())
print("圆的周长为:", circle.perimeter())