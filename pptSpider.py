# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:16:24 2018

@author: Wang
"""

import re
import requests
import hashlib
import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
p=ThreadPoolExecutor(30) #定义线程池最多容纳30个线程

#链接到第一ppt免费ppt模板的界面
def get_Index(url):
    respose=requests.get(url)
    if respose.status_code==200:
        print("网站链接成功")
        return respose.text
    else:
        print("无法链接到模板界面")
        return

#解析获取到的html代码，获取当前页面每个ppt模板的链接
def parse_Index(res):
    res=res.result()
    #获取模板链接
    urls=re.findall(r'h2.*?href="(.*?)"',res,re.S)
    # print(urls)
    for url in urls:
        #提交到线程池
        print(url)
        p.submit(get_Detail(url)) 

#模板详情界面        
def get_Detail(url):
    if not url.startswith('http'):
        url='http://www.1ppt.com%s' %url
    detailRespose=requests.get(url)
    if detailRespose.status_code==200:
        ppt_url=re.findall(r'class="downurllist".*?href="(.*?)"',detailRespose.text,re.S)
        ppt_url=ppt_url[0]
        if ppt_url:
            print(ppt_url)
            save('https://www.1ppt.com/'+ppt_url)
    #         ppt=requests.get(ppt_url)
    #         if ppt.status_code==200:
    #             m=hashlib.md5();
    #             m.update(ppt_url.encode('utf-8'))
    #             m.update(str(time.time()).encode('utf-8'))
    #             filename=r'%s.zip' % m.hexdigest()
    #             filepath=r'Z:\ppt\%s' %filename
    #             with open(filepath,'wb') as f:
    #                 f.write(ppt.content)
    #         else:
    #             print("无法下载")
    #             return
    # else:
    #     print("无法连接的详情界面")
    #     return
        
#将文件保存
def save(ppt_url):
    headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'Accept-Encoding':'gzip, deflate, br',
     'Accept-Language':'zh-CN,zh;q=0.9'
}
    ppt=requests.get(ppt_url,headers=headers)
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
def main():
    for i in range(5,7):
        p.submit(get_Index,'http://www.1ppt.com/moban/ppt_moban_%s.html' % i ).add_done_callback(parse_Index)
        # print(1)
        # p.submit(get_Index,'http://www.1ppt.com/moban/ppt_moban_%s.html' % i ).add_done_callback(parse_Index)

if __name__=='__main__':
    main()        

