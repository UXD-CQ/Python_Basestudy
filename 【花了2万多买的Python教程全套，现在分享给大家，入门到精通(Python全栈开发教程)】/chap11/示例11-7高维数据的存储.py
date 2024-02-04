import json
# 准备高维数据
lst=[
    {"name":"张三","age":20,"city":"北京"},
    {"name":"李四","age":25,"city":"上海"},
    {"name":"王五","age":30,"city":"广州"},
    {"name":"赵六","age":35,"city":"深圳"}
]
# 
s=json.dumps(lst,ensure_ascii=False,indent=4) # ensure_ascii正常显示中文 indent增加数据的缩进，美观实用，JSON格式字符串更有可读性
print(type(s),s) # 编码 list-->str 列表中是字典

# 解码
lst2=json.loads(s)
print(type(lst2),lst2)

# 编码到文件中
with open("student.txt","w",encoding="utf-8") as f:
    json.dump(lst,f,ensure_ascii=False,indent=4)

# 解码到程序
with open("student.txt","r",encoding="utf-8") as f:
    lst3=json.load(f)
print(lst3)
print(type(lst3))