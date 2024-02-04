from threading import Thread
a=100
def add():
    print('加线程开始执行')
    global a
    a+=30
    print(f'a的值为{a}')
    print('加线程执行完毕')

def sub():
    print('减线程开始执行')
    global a
    a-=30
    print(f'a的值为{a}')
    print('减线程执行完毕')

if __name__ == '__main__':
    print('主线程开始执行')
    print(f'a的初始值为{a}')
    add=Thread(target=add)
    sub=Thread(target=sub)
    add.start()
    sub.start()
    add.join()
    sub.join()
    print('主线程执行完毕')