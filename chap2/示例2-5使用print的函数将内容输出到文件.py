fp=open('note.word','w') # 打开文件 w--->write
print('我是李常卿，他是王晓峰',file=fp) # 将”我是李常卿“写入note.txt文件中 
fp.close() #关闭文件
