class Student():
    # 收尾双下划线
    def __init__(self, name, age, score):
        self._name = name # self.name受保护的，只能本类和子类访问
        self.__age = age # self.age表示私有的，只能本身去访问
        self.score = score # 普通的实例属性，类的内部，外部及子类都可访问
    
    def _fun1(self): # 这是一个受保护的函数
        print("子类及其本身可以访问")
    def __fun2(self): # 这是一个私有的函数
        print("只有定义的类可以访问")

    def show(self): # 普通的示例方法
        self._fun1() # 类本身访问受保护的方法
        self.__fun2() # 类本身访问私有方法
        print(self._name) # 受保护的实例属性
        print(self.__age) # 私有的实例属性

# 创建一个学生类的对象
stu=Student("张三",20,90)
# 类的外部
print(stu._name)
# print(stu.__age) # AttributeError: 'Student' object has no attribute '__age'. Did you mean: '_name'?

# 调用受保护的实例方法
stu._fun1() # 子类及其本身可以访问
# stu.__fun2() # AttributeError: 'Student' object has no attribute '__fun2'. Did you mean: '_fun1'?

# 私有的实例属性和方法是真的不能访问吗？
print(stu._Student__age)
stu._Student__fun2()

print(dir(stu))