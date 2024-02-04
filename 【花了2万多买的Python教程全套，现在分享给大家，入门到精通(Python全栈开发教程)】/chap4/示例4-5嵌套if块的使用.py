answer=input("请问您喝酒了吗？")
if answer=='y': #answer的值为y表示喝酒了
    proof=eval(input("请输入酒精含量："))
    if proof<20:
        print("没构成酒驾，祝你一路平安！")
    elif proof<80: # 20<=proof<=80
        print("构成酒驾，请不要开车！")
    else:
        print("构成酒驾，请自首！")
else:
    print("您没喝酒，祝您健康！")