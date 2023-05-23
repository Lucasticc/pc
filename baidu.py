import requests
import urllib3
import hashlib
import time
url1 = 'https://www.baidu.com/s?wd=1'
url2 = 'https://down.ypppt.com/uploads/soft/200830/1-200S0150238.zip'
url2 =  'https://ppt.1ppt.com/uploads/soft/2305/1-230505111318.zip'
http = urllib3.PoolManager()   # 创建连接池管理对象
headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'Accept-Encoding':'gzip, deflate, br',
     'Accept-Language':'zh-CN,zh;q=0.9'
}
r1 = http.request('GET', url2,headers=headers)    # 发送GET请求
def save(ppt_url):
    ppt=requests.get(url2,headers=headers)
    print(ppt)
    if ppt.status_code==200:
        m=hashlib.md5();
        m.update(ppt_url.encode('utf-8'))
        m.update(str(time.time()).encode('utf-8'))
        filename=r'%s.zip' % m.hexdigest()
        filepath=r'Z:\\ppt\\%s' %filename
        with open(filepath,'wb') as f:
            f.write(ppt.content)
    else:
        print("无法下载")
        return
save(url2)
