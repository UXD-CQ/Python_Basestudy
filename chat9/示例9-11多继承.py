class FatherA():
    def __init__(self,name):
        self.name = name

    def showA(self):
        print(f"FatherA name is {self.name}")

class FatherB:
    def __init__(self,age):
        self.age = age

    def showB(self):
        print(f"FatherB age is {self.age}")

# 多继承
class Son(FatherA,FatherB):
    def __init__(self,name,age,gender):
        # 需要调用两个父类的初始化方法
        FatherA.__init__(self,name)
        FatherB.__init__(self,age)
        self.gender = gender

son=Son("张三",20,"男")
son.showA()
son.showB()
print(son.name,son.age,son.gender)