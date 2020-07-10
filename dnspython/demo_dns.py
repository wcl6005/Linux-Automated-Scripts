# -*- coding: UTF-8 -*-
# pip install dnspython
# https://blog.csdn.net/xwl145/article/details/81746497?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# 


import dns.resolver

def dns_query(domain,type):
    try:
        A=dns.resolver.query(domain,type)
        for i in A.response.answer:
            for j in i:
                print (j)
    except dns.resolver.NoAnswer:
        print(domain+' 此域名，DNS未响应！')

dns_query('baidu.com','NS')
dns_query('baidu.com','A')
dns_query('163.com','MX')
dns_query('163.com','CNAME')
dns_query('www.uwintech.cn','CNAME')

"""
(env375) wuchunlongdeMacBook-Pro:dnspython wuchunlong$ python demo_dns.py
dns.baidu.com.
ns7.baidu.com.
ns3.baidu.com.
ns4.baidu.com.
ns2.baidu.com.
220.181.38.148
39.156.69.79
50 163mx00.mxmail.netease.com.
10 163mx02.mxmail.netease.com.
10 163mx03.mxmail.netease.com.
10 163mx01.mxmail.netease.com.
163.com 此域名，DNS未响应！
www.uwintech.cn.s.sxldns.com.


"""