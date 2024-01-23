x=True
print(x)
print(type(x)) # bool
print(x+10) #11 -->1+10
print(False+10) #10 -->0+10
print("---------------")
print(bool(18)) # true
print(bool(0),bool(0.0)) # false
#总结 非0的整数布尔值都是true
print(bool('北京欢迎你'))
print(bool(''))
#总结 所有非空字符串的布尔值都是true
print(bool(False))
print(bool(None))