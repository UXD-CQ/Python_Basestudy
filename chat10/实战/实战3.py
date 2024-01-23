'''
实战三:词云图
需求:使用Python第三方库
jieba与wordcloud实现对华为
笔记本评论的词云图
'''
import jieba
from wordcloud import WordCloud
# 读取数据
with open('/Users/ued_qing/Documents/PythonProject/chat10/华为笔记本.txt', 'r', encoding='utf-8') as f:
    s = f.read()
# 中文分词
lst=jieba.lcut(s)
# 排除词
stopword = ['一、购前须知1.购买渠道','2.被省略的信息','3.华为笔记本电脑购机优惠','二、华为笔记本品牌简介']
txt=''.join(lst)
# 绘制词云图
wordcloud=WordCloud(font_path='SimHei.ttf',background_color='white',width=1000,height=860,stopwords=stopword)

# 由txt生成词云图
wordcloud.generate(txt)
# 保存图片
wordcloud.to_file('华为笔记本.png')