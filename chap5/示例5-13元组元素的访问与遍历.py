t=('python','java','hello','male')
#根据索引访问元素
print(t[1])
t2=t[0:3:2]
print(t2)

#元组的遍历
for item in t:
    print(item)

for i in range(len(t)):
    print(i,t[i])

for index,item in enumerate(t,start=11):
    print(index,'-->',item)
