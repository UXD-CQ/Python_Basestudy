import weather
import openpyxl
html=weather.get_html() # 发请求，得响应结果
lst=weather.parse_html(html) # 解析数据

# 创建一个新的Excel工作簿
workbook = openpyxl.Workbook() # 创建对象
# 在Excel中创建一个工作表
sheet = workbook.create_sheet('景区天气')
# 向工作表中添加数据
for i in lst:
    sheet.append(i) # 一次添加一行

workbook.save('景区天气.xlsx')