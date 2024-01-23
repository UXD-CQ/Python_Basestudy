s='伟大的中国梦'
# 编码 str-->bytes
b=s.encode(errors='replace') #默认是utf-8,因为utf-8中文占用3个字节
print(b)

b_gbk=s.encode('gbk',errors='replace') #gbk中文占用2个字节
print(b_gbk)

# 编码中的出错问题
s2='耶✌🏻'
s2_gbk=s2.encode('gbk',errors='replace') # strict 会报错 ignore 会忽略 replace 会替换??
print(s2_gbk)

# 解码 bytes-->str
print(bytes.decode(b_gbk,'gbk'))
print(bytes.decode(b,'utf-8'))