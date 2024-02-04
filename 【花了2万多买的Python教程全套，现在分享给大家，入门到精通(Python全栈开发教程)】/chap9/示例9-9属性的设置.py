class Student:
    def __init__(self, name, age, corse):
        self.name = name
        self.__age = age

    # 使用@property 修饰方法 将方法转成属性使用
    @property
    def age(self):
        return self.__age
    
    # 将我们的age这个属性设置为可写属性
    @age.setter
    def age(self,value):
        if not isinstance(value,int):
            print('年龄必须为整数')
            self.__age = 0
        if value < 0 or value > 100:
            print('年龄范围不正确')
            self.__age = 0
        else:
            self.__age = value


stu=Student("张三", 20, "python")
print(stu.name,'年龄是：',stu.age) # stu.age就会去执行stu.age()
# 尝试修改属性值
# stu.age = 21 # AttributeError: property 'age' of 'Student' object has no setter

stu.age = 200
print(stu.name,'年龄是：',stu.age)

