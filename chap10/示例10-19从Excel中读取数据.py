import openpyxl
# 打开工作簿
workbook = openpyxl.load_workbook('景区天气.xlsx')
# 选择要操作的工作表
sheet = workbook['景区天气']
# 表格数据 是二维列表 先遍历行后遍历列
lst=[]
for row in sheet.rows:
    sublst=[]
    for cell in row: # cell指的是单元格
        sublst.append(cell.value)
    lst.append(sublst)

for i in lst:
    print(i)