import os
import requests
from bs4 import BeautifulSoup
 
if not os.path.exists('./images/'):
    os.mkdir('./images/')
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
}
 
url = 'http://wx4.sinaimg.cn/large/ceeb653ely8gw2o2b5f61j20jz0j5dgr'
 
response = requests.get(url, headers=headers)
 
name = '图片.jpg'
with open(f'./images/{name}', 'wb')as f:
    f.write(response.content)