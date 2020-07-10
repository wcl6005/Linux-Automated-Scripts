# -*- coding: UTF-8 -*-
# 比较文件内容，并显示


import sys
import difflib
import filecmp

def read_file(filename):
    """ 读文件 """
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except IOError:
        print("ERROR: 没有找到文件:%s或读取文件失败！" % filename)
        sys.exit(1)

def compare_file(file1, file2, out_file):
    """ 比较文件内容 """
    file1_content = read_file(file1)
    file2_content = read_file(file2)
    d = difflib.HtmlDiff()
    result = d.make_file(file1_content, file2_content)
    with open(out_file, 'w') as f:
        f.writelines(result)
    print('OK! %s success.' %out_file)


def file_cmp(file1, file2, shallow):
    """
    单文件对比
    采用filecmp.cmp(f1, f2[, shallow])方法，比较文件名为f1和f2的文件，相同返回True，不同返回False。
    shallow默认为True，即只根据os.stat()方法返回的文件基本信息（最后访问时间、修改时间、状态改变时间等）进行对比，而忽略文件内容的对比 ???
    当shallow为False时，则同时校验os.stat()与文件内容。
    filecmp.cmp(master, other, False)
    https://blog.csdn.net/chengqiuming/article/details/87474806?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-9
    """    
    return filecmp.cmp(file1, file2, shallow)


def file_cmpfiles(dir1,dir2,lis,shallow=True):
    """
    比较两个文件夹内指定文件是否相等
    lis=['f1','f2','f3','f4','f5',shallow=True]
    采用filecmp.cmpfiles（dir1，dir2，common[， shallow]）方法，对比dir1与dir2目录给定的文件清单。该方法返回文件名的三个列表，分别为匹配、不匹配、错误。匹配为包含匹配的文件的列表，不匹配反之，错误列表包括了目录不存在文件、不具备读权限或其他原因导致的不能比较的文件清单。

    我们构造两个目录中的f1、f2、f3文件相同，f4和f5文件不同。
    https://blog.csdn.net/chengqiuming/article/details/87474806?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-9
    """
    
    return filecmp.cmpfiles(dir1,dir2,lis,shallow)
     



if __name__ == '__main__':
    compare_file('file1.py', 'file2.py', 'result.html')
    print(file_cmp('./dir1/creat_file.txt', './dir2/creat_file.txt',True))  #  不校验文件内容
    print(file_cmp('./dir1/creat_file.txt', './dir2/creat_file.txt', False))  # 校验os.stat()与文件内容

    lis = ['f1.txt','f2.txt','f3.txt','f4.txt','f5.txt','creat_file.txt']
    print(file_cmpfiles('dir1','dir2',lis))
    print(file_cmpfiles('dir1','dir2',lis, False))
   

 
"""
存在问题：shallow=False  shallow=True  结果一样，不知什么原因？？？
(env375) wuchunlongdeMacBook-Pro:difflib wuchunlong$ python creat_file.py
(env375) wuchunlongdeMacBook-Pro:difflib wuchunlong$ python diff_file.py
True
True
(['f1.txt', 'creat_file.txt'], ['f2.txt', 'f3.txt'], ['f4.txt', 'f5.txt'])
(['f1.txt', 'creat_file.txt'], ['f2.txt', 'f3.txt'], ['f4.txt', 'f5.txt'])
列表[0] == 匹配
列表[1] == 不匹配
列表[2] == 不存在，无法比较

"""