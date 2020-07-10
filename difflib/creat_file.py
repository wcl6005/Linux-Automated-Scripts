# -*- coding: UTF-8 -*-

def writetxt(filename,txt):
    """
    w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    """ 
    ret = False
    with open(filename,'w+') as f:
        f.write(txt)
        ret = True
    return ret

# 同时在不同目录下，创建两个文件名一样的文件，但是文件内容不同。
writetxt('./dir1/creat_file.txt','hello world')
writetxt('./dir2/creat_file.txt','hello world')