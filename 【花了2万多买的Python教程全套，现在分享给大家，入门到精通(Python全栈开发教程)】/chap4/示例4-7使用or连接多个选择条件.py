score=eval(input("请输入成绩："))
if 0>score or score>100:
    print("输入的成绩无效！")
else:
    print("您的成绩为：",score)