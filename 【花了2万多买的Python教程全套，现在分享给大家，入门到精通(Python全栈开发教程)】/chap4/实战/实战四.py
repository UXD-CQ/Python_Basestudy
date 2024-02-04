print('-'*10,'猜数游戏','-'*10)
import random
target = random.randint(1,100)
count = 0
while count<10:
    guess = int(input('在我心中有个数，1-100之间，请您猜一猜：'))
    if guess == target:
        print('恭喜你，猜对了！','您用了',count,'次')
        break
    elif guess<target:
        print('猜小了！')
    else:
        print('猜大了！')
    count += 1
else:
    print('很遗憾，您没有在规定次数内猜对！')
    print('正确答案是：',target)