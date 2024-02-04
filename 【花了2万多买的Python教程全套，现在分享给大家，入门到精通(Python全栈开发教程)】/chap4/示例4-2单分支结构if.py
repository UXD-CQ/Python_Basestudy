number=eval(input("请输入您的6位中奖号码："))
#使用if语句
if number==521321:
    print("恭喜您，中奖了！")

if number!=521321:
    print("很遗憾，未中奖！")
print('-'*10,'以上if判断的表达式，是通过比较运算符计算出来的，结果是布尔值类型','_'*10)
n=98 #赋值操作
if n%2:
    print(n,"n是奇数")
if not n%2:
    print(n,"n是偶数")
print('-'*10,'判断一个字符串是否是空字符串','_'*10)
x=input("请输入一个字符串：")
if x:
    print("x不是空字符串")
if not x:
    print("x是空字符串")
print('-'*10,'表达式也可以是一个单纯的布尔型变量','_'*10)
flag=eval(input("请输入一个布尔表达式：Ture或False"))
if flag:
    print("表达式的结果是True")
if not flag:
    print("表达式的结果是False")
print('-'*10,'使用if语句时，如果语句块中只有一句代码，可以将语句块直接写在冒号后面','_'*10)
a=10
b=5
if a>b:max=a
print("a大于b，a的最大值是：",max)

