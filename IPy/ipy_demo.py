# -*- coding: UTF-8 -*-
# 根据IP地址和子网掩码算出网段
# python ip地址和子网掩码求网络号  https://www.uguu.com/article-326894.html


import re
from IPy import IP


# def is_ip(ipAddr): 
#     #判定IP地址合法性
#     try: 
#         IP(ipAddr) # IP('127.0') 不报错,不采用此方法。
#         return True
#     except Exception as ex:
#         return False

def is_ip(ipAddr): 
    """ 判定IP地址合法性 """
    compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        return True 
    else:  
        return False    

def network_segment():
    ip_address = input('请输入ip地址:')
    if not is_ip(ip_address):
        print("您输入的ip地址不合法，请重新输入！")
        exit()

    netmask_address = input('请输入子网掩码:')
    if not is_ip(netmask_address):
        print("您输入的子网掩码不合法，请重新输入！")
        exit()

    return IP(ip_address).make_net(netmask_address)


if __name__ == '__main__':
    net_segment = network_segment()
    print("您所在的网段为:%s" %net_segment)

"""
(env375) wuchunlongdeMacBook-Pro:IPy wuchunlong$ python ipy_demo.py
请输入ip地址:192.168.1.1
请输入子网掩码:255.255.252.0
您所在的网段为:192.168.0.0/22

"""