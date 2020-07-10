# -*- coding: UTF-8 -*-
# 官网：  https://github.com/giampaolo/psutil

import psutil
import time

def get_cpu():
    for x in range(3):
        time.sleep(1)
        cpu_liyonglv = psutil.cpu_percent(interval=1)
        print("当前cpu利用率：\033[1;31;42m%s%%\033[0m"%cpu_liyonglv)


def memissue():    
    mem= psutil.virtual_memory()
    #单位换算为MB
    memtotal= mem.total/1024/1024
    memused = mem.used/1024/1024
    membaifen = mem.percent
    print("内存信息:")
    print("%.1fMB"% memtotal)
    print("%.1fMB"% memused)
    print("%.1f%%"%(membaifen))

def disklist():
    #disk = psutil.disk_partitions()
    diskuse= psutil.disk_usage('/')
    #单位换算为GB
    diskused= diskuse.used/1024/1024/1024
    disktotal= diskuse.total/1024/1024/1024
    diskbaifen = diskuse.percent
    print("磁盘信息:")
    print('%.2fGB'% diskused)
    print('%.2fGB'% disktotal)
    print('%.2f%%' % (diskbaifen))




if __name__ == '__main__':
    get_cpu()
    print('*'*20)
    memissue()
    print('*'*20)
    disklist()
    

