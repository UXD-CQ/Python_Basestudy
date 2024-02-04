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

# Doctor继承Person类
class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


# 创建Student对象
stu1 = Student("张三", 20, "2021001")
stu1.my_func()
doctor= Doctor("李四", 30, "内科")
doctor.my_func()