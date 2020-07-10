# -*- coding: UTF-8 -*-

import time
import os

def name():
	"""
    生成磁盘使用情况的日志文件
	"""
	new_time = time.strftime('%Y-%m-%d[%H:%M:%S]')
	disk_status = os.popen('df -h').readlines()
	str1 = ''.join(disk_status)
	filename = '%s.log' %new_time
	f = open(filename,'w+')
	f.write('%s' %str1)
	f.flush()
	f.close()
	print('OK! 生成磁盘使用情况的%s日志文件.' %filename)


if __name__ == '__main__':
    name()
