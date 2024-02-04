import threading
from threading import Thread
import time
ticket = 50 # 代表总共50张车票

def sell_ticket():
    global ticket
    # 每个排队窗口假设有100人
    for i in range(100):
        if ticket > 0:
            print(f'{threading.current_thread().name}正在出售第{ticket}张车票')
            ticket -= 1
            time.sleep(1)

if __name__ == '__main__':
    for i in range(3): # 循环执行3次
        t = Thread(target=sell_ticket)
        t.start()