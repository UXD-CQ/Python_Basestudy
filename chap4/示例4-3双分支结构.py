number=eval(input("请输入您的6位中奖号码："))
# if...else...
if number==123456:
    print("恭喜您中奖了！")
else:
    print("很遗憾，您没有中奖。")
print('-'*10,'以上代码可以使用条件表达式进行简化','_'*10)
result='恭喜您中奖了！' if number==123456 else '很遗憾，您没有中奖。'
print(result)