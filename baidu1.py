
import urllib3
from lxml import etree
 
url = ('https://www.baidu.com/')
http = urllib3.PoolManager()   # 创建连接池管理对象

 
headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'Accept-Encoding':'gzip, deflate, br',
     'Accept-Language':'zh-CN,zh;q=0.9'
}
 
req = http.request('GET',url=url,headers=headers)
content = req.content.decode('utf-8')
 
 
get = etree.HTML(content)
geturl = get.xpath('//div[@id="s-top-left"]/a/@href')
getname = get.xpath('//div[@id="s-top-left"]/a/text()')
works=[]
for urls,names in zip(geturl,getname):
    work={
        "url":urls,
        "name":names
    }
    works.append(work)
print(work)