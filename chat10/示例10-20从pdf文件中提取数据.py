import pdfplumber
# 打开PDF文件
with pdfplumber.open('xiaoxue.pdf') as pdf:
    for i in pdf.pages: # 遍历项
        print(i.extract_text()) # extract_text()方法提取内容
        print(f'-----------第{i.page_number}页结束')