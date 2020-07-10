# -*- coding: UTF-8 -*-

import os
import time
import sys
import pycurl

def name(URL):
    """
    该脚本可以定位访问web页面的服务质量
    通过Python下的pycurl模块来实现定位
    它可以通过调用pycurl提供的方法，来探测Web服务质量
    比如了解相应的HTTP状态码、请求延时、HTTP头信息、下载速度等

    python3.7.5 测试通过
    """

    # 创建一个Curl对象
    c = pycurl.Curl()
    # 定义请求的URL变量
    c.setopt(pycurl.URL, URL)
    # 定义请求连接的等待时间
    c.setopt(pycurl.CONNECTTIMEOUT, 5)
    # 定义请求超时时间
    c.setopt(pycurl.TIMEOUT, 5)
    # 屏蔽下载进度条
    c.setopt(pycurl.FORBID_REUSE, 1)
    # 指定HTTP重定向的最大数为1
    c.setopt(pycurl.MAXREDIRS, 1)
    # 完成交互后强制断开连接，不重用
    c.setopt(pycurl.NOPROGRESS, 1)
    # 设置保存DNS信息的时间为30秒
    c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)

    # 创建一个文件对象，以“wb”方式打开，用来存储返回的http头部及页面的内容
    indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")
    # 将返回的HTTP HEADER定向到indexfile文件
    c.setopt(pycurl.WRITEHEADER, indexfile)
    # 将返回的HTML内容定向到indexfile文件
    c.setopt(pycurl.WRITEDATA, indexfile)

    # 捕捉Curl.perform请求的提交，如果错误直接报错退出
    try:
        c.perform()
    except Exception as ex:
        print("连接错误 %s"%ex)
        indexfile.close()
        c.close()
        sys.exit()

    # DNS解析所消耗的时间
    NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
    # 建立连接所消耗的时间
    CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
    # 从建立连接到准备传输所消耗的时间
    PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
    # 从建立连接到传输开始消耗的时间
    STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
    # 传输结束所消耗的总时间
    TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
    # 返回HTTP状态码
    HTTP_CODE = c.getinfo(c.HTTP_CODE)
    # 下载数据包的大小
    SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
    # HTTP头部大小
    HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
    # 平均下载速度
    SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

    indexfile.close()
    c.close()

 
    return """
    HTTP状态码：%d 
    DNS解析时间：%.2f ms 
    建立连接时间：%.2f ms 
    准备传输时间：%.2f ms 
    传输开始时间：%.2f ms 
    传输结束总时间：%.2f ms 
    下载数据包大小：%d bytes/s 
    HTTP头部大小：%d byte 
    平均下载速度：%d bytes/s 
    """ %(HTTP_CODE, NAMELOOKUP_TIME*1000, CONNECT_TIME*1000, 
        PRETRANSFER_TIME*1000, STARTTRANSFER_TIME*1000, TOTAL_TIME*1000, 
        SIZE_DOWNLOAD, HEADER_SIZE, SPEED_DOWNLOAD)

if __name__ == '__main__':
    # 探测目标URL
    URL = "http://www.baidu.com" 
    items = name(URL)
    print(items)


"""
(env375) wuchunlongdeMacBook-Pro:probe-web-service-quality wuchunlong$ python  probe_web_service_quality.py
   
    HTTP状态码：200 
    DNS解析时间：18.01 ms 
    建立连接时间：30.08 ms 
    准备传输时间：30.25 ms 
    传输开始时间：56.07 ms 
    传输结束总时间：140.11 ms 
    下载数据包大小：245334 bytes/s 
    HTTP头部大小：1197 byte 
    平均下载速度：1752385 bytes/s 

"""
