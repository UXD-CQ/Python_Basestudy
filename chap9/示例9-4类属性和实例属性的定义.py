class Student():
    # 类属性：定义在类中，方法外的变量
    school='北京XXX教育'

    # 初始化方法
    def __init__(self,name,age): # name，age是方法的参数，是局部变量 作用域是整个__init__方法
    self.name1=name # 左侧是实例属性 name是局部变量 将局部变量的值name赋值给实例属性self.name1
    selt.age=age # 示例名称和局部变量可以相同

    # 实例9-5类的组成
    # 定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫:{self.name1},今年:{self.age}岁了')

    # 静态方法
    @staticmethod
    def printinfo():
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')

    # 类方法
    @classmethod
    def printinfo1(cls):
        print('这是一个类方法，不能调用实例属性，也不能调用实例方法')

# 创建类的对象
stu1=Student('张三',20)
# 实例属性，使用对象名进行打点调用
print(stu1.name1,stu1.age)
# 类属性，直接使用类名，打点调用
print(Student.school)

# 实例方法，使用对象名进行打点调用
stu1.show()
# 类方法 @classmethod进行修饰的方法 直接使用类名打点调用
Student.cm()
# 静态方法 @staticmethod进行修饰的方法 直接使用类名打点调用
Student.sm()