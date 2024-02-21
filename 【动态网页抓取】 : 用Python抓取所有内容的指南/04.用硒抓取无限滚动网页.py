from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import time 

options = webdriver.ChromeOptions() 
options.headless = True 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 

# 加载目标网站 
url = 'https://scrapingclub.com/exercise/list_infinite_scroll/' 

# 获取网站内容 
driver.get(url) 

# 实例化项目 
items = [] 

# 实例化网页的高度 
last_height = driver.execute_script('return document.body.scrollHeight') 

# 设定目标计数
itemTargetCount = 20 

# 滚动到网页底部
while itemTargetCount > len(items): 
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') 

	# 等待内容加载

	time.sleep(1) 

	new_height = driver.execute_script('return document.body.scrollHeight') 

	if new_height == last_height: 
		break 

	last_height == new_height 

	# 通过 XPath 选择元素 
	elements = driver.find_elements(By.XPATH, "//div[@class='p-4']/h4/a") 
	h4_texts = [element.text for element in elements] 

	items.extend(h4_texts) 

	# 打印标题
	print(h4_texts)