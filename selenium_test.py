from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baidu_search = {
    'button_search':'//input[@value = "百度一下"]',
    'input_search':'//input[@name = "wd"]'
    }
#指定chromedriver路径
chrome_driver_path = "/Users/worker/chromedriver/chromedriver-mac-x64/chromedriver"
service = Service(chrome_driver_path)

chrome_options = Options()
chrome_options.add_argument('--remote-debugging-port=9222') # 指定端口
chrome_options.add_argument('--start-maximized')
# chrome_options.add_experimental_option('detach',True) # 流程结束时不关闭浏览器
chrome_options.add_experimental_option('excludeSwitches',['enable-automation']) # 禁用浏览器自动更新检查

# 初始化 Chrome 浏览器
driver = webdriver.Chrome(service = service,options=chrome_options)
driver.get("https://www.baidu.com") # 打开网站

# 查找网页元素
driver.maximize_window()
# driver.switch_to.frame("") # 切换iframe框架
input_search_element = driver.find_element(By.XPATH,baidu_search.get('input_search'))
input_search_element.send_keys('selenium')
button_search = driver.find_element(By.XPATH,baidu_search.get('button_search'))
button_search.click()

time.sleep(5)
# driver.quit()