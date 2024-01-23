print('-'*10,'根据父母身高预测儿子身高','-'*10)
father_height = eval(input('请输入父亲身高：'))
mother_height = eval(input('请输入母亲身高：'))
son_height = (father_height + mother_height) * 0.54
print('预测儿子身高：',son_height)