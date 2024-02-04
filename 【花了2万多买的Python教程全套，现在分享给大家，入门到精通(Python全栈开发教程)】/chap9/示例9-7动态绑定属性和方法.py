class Student:
    school='北京XXX教育'
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def show(self):
        print(f'姓名：{self.name},年龄：{self.age},成绩：{self.score}')
# 创建两个student对象
stu=Student('张三',20,90)
stu2=Student('李四',22,85)
print(stu.name,stu.age,stu.score)
print(stu2.name,stu2.age,stu2.score)

# 为stu2动态绑定一个实例
stu2.gender='男'
print(stu2.name,stu2.age,stu2.score,stu2.gender)

# 动态绑定方法
def introduce():
    print('我是一个普通的函数，我被动态绑定成了stu2对象的方法')
stu2.fun=introduce # 函数的一个赋值
# fun就是stu2对象的方法
# 调用
stu2.fun()
