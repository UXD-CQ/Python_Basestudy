# coding: UTF-8
# 定义学生类录入5个学生信息存储到列表中
class Student:
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score
    # 示例方法 用于输出信息
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Score: {self.score}")

print('请输入5位学生信息：（姓名#年龄#性别#成绩）')
lst = [] # 用于储存5个学生对象
for i in range(5):
    s=input(f'请输入第{i}位学生的信息：')
    s_lst=s.split('#')
    # 创建学生对象
    stu=Student(s_lst[0], s_lst[1], s_lst[2], s_lst[3])
    # 将学生对象添加到列表中
    lst.append(stu)

# 遍历对象，调用学生对象的info方法
for stu in lst:
    stu.info()