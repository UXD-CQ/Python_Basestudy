from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 

# 实例化选项
options = webdriver.ChromeOptions() 

# 以无头模式运行浏览器
options.headless = True 

# 实例化驱动程序 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 

# 加载网站
url = 'https://angular.io/' 

# 获取整个网站内容
driver.get(url) 

# 按类名选择元素 
elements = driver.find_elements(By.CLASS_NAME, 'text-container') 
for title in elements: 
	# 在元素内按标签名称选择 H2s
	heading = title.find_element(By.TAG_NAME, 'h2').text 
	# 打印 
	print(heading)