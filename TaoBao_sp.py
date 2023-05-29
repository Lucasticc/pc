from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开淘宝网的商品搜索页面
driver.get('https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA')

# 模拟向下滚动页面
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# 解析页面内容
soup = BeautifulSoup(driver.page_source, 'html.parser')
items = soup.find_all('div', {'class': 'item'})

# 输出商品信息
for item in items:
    title = item.find('a', {'class': 'title'}).text.strip()
    price = item.find('div', {'class': 'price'}).text.strip()
    print(title, price)

# 关闭浏览器
driver.quit()