class Student:
    school="北京XXX学校"
    def __init__(self,xm,age):
        self.name=xm
        self.age=age
    def show(self):
        print(f'我叫:{self.name},今年{self.age}岁了')

# 创建多个对象
stu1=Student("张三",20)
stu2=Student("李四",22)
stu3=Student("王五",25)
stu4=Student("赵六",29)

print(type(stu1))
print(type(stu2))
print(type(stu3))
print(type(stu4))

Student.school='森派教育' # 给类的类属性赋值

# 将学生对象存储到列表中
lst=[stu1,stu2,stu3,stu4] # 列表中的元素是Student类型的对象
for item in lst: # item是列表中的元素，是Student类型的对象
    item.show() # 对象名打点调用实例方法

