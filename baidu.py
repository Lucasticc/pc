import requests
import urllib3
import re
url1 = 'https://www.baidu.com/s?wd=1'
url2 = 'https://ppt.1ppt.com/uploads/soft/2305/1-230505111318.zip'
# url2 =  'https://www.1ppt.com/plus/download.php?open=0&aid=106164&cid=3'
url_name = 'https://www.1ppt.com/article/106164.html#xiazai'
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
        #搞个md5只是为了不重复 我也是服了
        # filename=r'%s.zip' % m.hexdigest()
        ppt_name = requests.get(url_name,headers=headers)
        file_name =re.findall(r'<title>(.*?)</title>',ppt_name.content.decode('utf-8'))
        file_name = file_name[0]
        print(file_name)
        filename=r'%s.zip' %file_name
        filepath=r'Z:\\ppt\\%s' %filename
        # filepath=r'Z:\\ppt\\%s.zip' 
        with open(filepath,'wb') as f:
            f.write(ppt.content)
    else:
        print("无法下载")
        return
save(url2)
