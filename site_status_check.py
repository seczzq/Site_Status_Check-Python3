#!/usr/bin/python3
# -*- coding:utf-8 -*-
# for check wangguan site status
# The author :zzq
###################################################################################
###本程序旨在对网站运行状态批量进行检查，优化现场服务，提高现场工作执行效率！
###程序开发使用python3环境进行开发，开发时间为：2019年11月06日
###如有问题可联系邮箱：ziqiang.zhang@ingeek.com
###################################################################################

import requests
import time
import sys
localtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
reports = open(localtime+'.txt','w+',encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

def check_url(url):
    try:
        url_requests = requests.get(url=url,headers=headers,timeout=3)
        if url_requests.status_code == 200:
            good.append(url)
        else:
            site_bad.append(url)
    except Exception as e:
        server_bad.append(url)
def banner():
    site_status = r''' site:www.ingeek.com
-----------------------------------------------------------------------------------
    本程序旨在对网站运行状态批量进行检查，优化现场服务，提高现场工作执行效率！
    程序开发使用python3环境进行开发，开发时间为：2019年11月06日
    如有问题可联系邮箱：ziqiang.zhang@ingeek.com 
-----------------------------------------------------------------------------------
            '''.format()
    print(site_status)

if __name__ == '__main__':
    banner()
    url_files = open(r'urls.txt','r')
    good = []
    server_bad = []
    site_bad = []
    for url in url_files.readlines():
        url = url.strip()
        sys.stdout.write("\r #小基正在火速检查:    "+url)
        sys.stdout.flush()
        check_url(url)
    time.sleep(2)
    sys.stdout.write("\r #小基正在火速检查:  全部检查完毕！                                                                 \n")
    sys.stdout.flush()
    for i in range(len(good)):
        reports.write(str(good[i])+ '     网站正常运行! \n')
        print('\n\n检查结果如下：\n')
        print(good[i]+'     网站正常运行!')
    for i in range(len(server_bad)):
        reports.write(str(server_bad[i]) + '     服务器关闭状态! \n')
        print(server_bad[i] + '     服务器关闭状态! ')
    for i in range(len(site_bad)):
        reports.write(str(site_bad[i]) + '     服务器开启状态，网站停止运行! \n')
        print(site_bad[i]+'     服务器开启状态，网站停止运行!')
    reports.close()
    url_files.close()
