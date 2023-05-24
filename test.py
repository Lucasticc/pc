import requests
import json
import re
url = 'https://www.1ppt.com/article/106164.html#xiazai'
headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'Accept-Encoding':'gzip, deflate, br',
     'Accept-Language':'zh-CN,zh;q=0.9'
}
ppt = requests.get(url=url,headers=headers)
# print(ppt.content.decode('utf-8'))
print(ppt.text.encode('utf-8'))
# print(re.findall(r'<title>(.*?)</title>',ppt.content.decode('utf-8')))
# print(ppt.content.decode('utf-8'))
# print(ppt.text.find('title'))