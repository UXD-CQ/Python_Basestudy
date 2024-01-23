# 使用面向对象思想实现乐器弹奏
class Instrument:
    def make_sound(self):
        pass

class Erhu(Instrument):
    def make_sound(self):
        print("二胡在弹奏")

class Pinao(Instrument):
    def make_sound(self):
        print("钢琴在演奏")

class Violin(Instrument):
    def make_sound(self):
        print("小提琴在拉奏")

# 编写一个函数
def play(obj):
    obj.make_sound()

# 测试
er=Erhu()
pin=Pinao()
vio=Violin()

# 调用方法
play(er)
play(pin)
play(vio)
