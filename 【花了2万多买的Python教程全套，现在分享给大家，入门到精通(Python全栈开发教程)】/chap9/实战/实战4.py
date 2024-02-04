# 请使用面向对象的思想，设计自定义类，描述出租车和家用轿车的信息
# 出租车类：属性包括：车型，车牌，所属出租公司；方法包括：启动，停止
# 家用轿车类：属性包括：车型，车牌，车主姓名；方法包括：启动，停止
class Car(object):
    def __init__(self, type,no):
        self.type = type
        self.no = no

    def start(self):
        print(f"我是车，我能启动")
    def stop(self):
        print(f"我是车，我能停止")

# 出租车
class Taxi(Car):
    def __init__(self, type, no, company):
        super().__init__(type, no)
        self.company = company
    # 重写父类的启动和停止的方法
    def start(self):
        super().start()
        print('乘客您好！')
        print(f"我是{self.type}，车牌是{self.no}，属于{self.company}公司，我已启动")
    def stop(self):
        super().stop()
        print('目的地到了，请您扫码付款，欢迎下次乘坐')

# 家用轿车
class Sedan(Car):
    def __init__(self, type, no, name):
        super().__init__(type, no)
        self.name = name

    def start(self):
        print(f'我是{self.name}，我的轿车我做主')
    def stop(self):
        print('目的地到了，我们去玩儿吧！')

# 测试
Taxi = Taxi('出租车', '京A1234', '长城')
Taxi.start()
Taxi.stop()

print('----------------------')
Sedan = Sedan('广汽丰田', '沪B5678', '张三')
Sedan.start()
Sedan.stop()