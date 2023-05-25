import requests
import json
import re
headers = {
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding':'gzip, deflate, br',
          'Accept-Language':'zh-CN,zh;q=0.9'
     }
def save(ppt_url,ppt_name):
    ppt=requests.get(ppt_url,headers=headers)
    if ppt.status_code==200:
        filename=r'%s.zip' %ppt_name
        filepath=r'Z:\\ppt\\%s' %filename
        with open(filepath,'wb') as f:
            f.write(ppt.content)
    else:
        print("无法下载")
        return
def get_url(url):
     url = 'https://www.ypppt.com/article/2020/6816.html'
     headers = {
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding':'gzip, deflate, br',
          'Accept-Language':'zh-CN,zh;q=0.9'
     }
     ppt = requests.get(url='https://www.ypppt.com'+url,headers=headers)
     ppt.encoding = 'utf-8'
     pattern = r'/p/d\.php\?aid=\d+'
     url1='https://www.ypppt.com/'+re.findall(pattern,ppt.text)[0]
     ppt_name=re.findall(r'<title>(.*?)</title>',ppt.text)
     url2 = requests.get(url=url1,headers=headers)
     down_url = re.findall(r'https://down\.ypppt\.com/uploads.*?\.zip',url2.text)
     if len(down_url) == 0:
          down_url = re.findall(r'https://down\.ypppt\.com/uploads.*?\.rar',url2.text)
     print(ppt_name,down_url[0])
     return ppt_name,down_url

# print(ppt.content.decode('utf-8'))
# print(ppt.text.encode('utf-8'))
# print(re.findall(r'<title>(.*?)</title>',ppt.content.decode('utf-8')))