class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Student继承Person类
class Student(Person):
    def __init__(self, name, age, stuno):
        super().__init__(name, age)
        self.stuno = stuno

    def my_func(self):
        # 调用父类中的方法
        super().my_func()
        print(f"My student number is {self.stuno}.")

# Doctor继承Person类
class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def my_func(self):
        # 调用父类中的方法
        # super().my_func
        print(f"大家好，我叫：{self.name}，我今年{self.age}岁了，我的工作科室是{self.department}")

# 创建Student对象
stu1 = Student("张三", 20, "2021001")
stu1.my_func() # 调用子类自己的my_func方法
doctor= Doctor("李四", 30, "内科")
doctor.my_func() # 调用子类自己的my_func方法