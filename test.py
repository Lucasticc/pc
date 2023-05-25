import requests
import re
import json
url = 'https://www.ypppt.com/p/d.php?aid=2768'
headers = {
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding':'gzip, deflate, br',
          'Accept-Language':'zh-CN,zh;q=0.9'
     }
url2 = requests.get(url=url,headers=headers)
url2.encoding = 'utf-8'
down_url = re.findall(r'https://down\.ypppt\.com/uploads.*?\.zip',url2.text)
if len(down_url) == 0:
     down_url = re.findall(r'https://down\.ypppt\.com/uploads.*?\.rar',url2.text)

print(down_url[0])