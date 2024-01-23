class Person(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'大家好，我是{self.name}，今年{self.age}岁了')

# 创建Person对象
per = Person('张三',20) # 创建对象的时候会自动创建__init__方法()
print(dir(per))

print(per) # 自动调用__str__方法