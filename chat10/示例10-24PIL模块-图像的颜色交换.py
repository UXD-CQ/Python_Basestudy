from PIL import Image
# 加载图片
image = Image.open('google.jpg')
# print(type(image),image)
# 提取RGB图像的颜色通道,返回结果是图像的副本
r = image.split()[0]
g = image.split()[1]
b = image.split()[2]
# print(red_channel,green_channel,blue_channel)
# 合并通道
merged_image = Image.merge('RGB', (r, b, g))
merged_image.save('new_image.jpg')
