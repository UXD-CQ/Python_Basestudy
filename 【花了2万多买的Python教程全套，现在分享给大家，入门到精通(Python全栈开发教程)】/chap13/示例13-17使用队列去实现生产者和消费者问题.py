from queue import Queue
from threading import Thread
import time
# 创建一个生产者类
class Producer(Thread):
    def __init__(self, name,queue):
        Thread.__init__(self, name=name)
        self.queue = queue
    def run(self):
        for i in range(1,6):
            print(f"{self.name}将产品{i}放入队列")
            self.queue.put(i)
            time.sleep(1)
        print('生产者完成了所有数据存放')
# 创建一个消费者类
class Consumer(Thread):
    def __init__(self, name,queue):
        Thread.__init__(self, name=name)
        self.queue = queue
    def run(self):
        for i in range(5):
            val = self.queue.get()
            print(f"消费者线程：{self.name}取出了产品{val}")
            time.sleep(1)

if __name__ == '__main__':
    # 创建队列
    queue=Queue()
    # 创建生产者线程
    p1=Producer("生产者1",queue)
    # 创建消费者线程
    c1=Consumer("消费者1",queue)

    # 启动线程
    p1.start()
    c1.start()
    # 等待线程结束
    p1.join()
    c1.join()
    print("主线程结束")