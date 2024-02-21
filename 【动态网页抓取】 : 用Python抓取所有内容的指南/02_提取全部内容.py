# 导入selenium库
from selenium import webdriver 
# 导入selenium库中Chrome浏览器的service
from selenium.webdriver.chrome.service import Service as ChromeService 
# 导入webdriver_manager库中的ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager 

# 定义要访问的网址
url = 'https://angular.io/' 

# 使用Chrome浏览器，并使用webdriver_manager库来管理ChromeDriver
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 

# 打开网址
driver.get(url) 

# 打印页面源代码
print(driver.page_source)