#!/usr/bin/env python3
# coding: utf-8

import os
from urllib.request import urlopen

import requests
from tqdm import tqdm
def download_from_url(url, dst):
    """
    @param: url to download file
    @param: dst place to put the file
    :return: bool
    """
    # 获取文件长度
    try:
        file_size = int(urlopen(url).info().get('Content-Length', -1))
    except Exception as e:
        print(e)
        print("错误，访问url: %s 异常" % url)
        return False

    # 文件大小
    if os.path.exists(dst):
        first_byte = os.path.getsize(dst)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'Accept-Encoding':'gzip, deflate, br',
     'Accept-Language':'zh-CN,zh;q=0.9',
        "Range": "bytes=%s-%s" % (first_byte, file_size)}
    pbar = tqdm(
        total=file_size, initial=first_byte,
        unit='B', unit_scale=True, desc=url.split('/')[-1])

    # 访问url进行下载
    req = requests.get(url, headers=header, stream=True)
    try:
        with(open(dst, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
    except Exception as e:
        print(e)
        return False

    pbar.close()
    return True

if __name__ == '__main__':
    url = "https://ppt.1ppt.com/uploads/soft/2305/1-230522161P8.zip"
    # url = "https://dl.360safe.com/360/inst.exe"
    download_from_url(url, "inst.exe")