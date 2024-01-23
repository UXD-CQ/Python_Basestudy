class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 方法重写
    def __str__(self):
        return f'Person: name={self.name}, age={self.age}' # 返回值是一个字符
# 创建Person类的对象
per = Person('Alice', 20)
print(per) # 还是内存地址吗？不是，__str__方法中的内容 直接输出对象名，实际上是调用的__str__方法
print(per.__str__())
