# -*- coding: UTF-8 -*-

"""
@desc 使用filecmp.dircmp递归比对两个目录，输出比对结果以及统计信息。
@author wuchunlong
@date 2020-6-14




dircmp#提供了三个方法用于报告比较的结果：
report()：#只比较指定文件夹中的内容（文件与文件夹）
report_partial_closure()：#比较文件夹及第一级子文件夹的内容
report_full_closure()：#递归比较所有的文件夹的内容

复制代码

#dircmp还提供了下面这些属性用于获取比较的详细结果
left_list：#左边文件夹中的文件与文件夹列表；
right_list：#右边文件夹中的文件与文件夹列表；
common：#两边文件夹中都存在的文件或文件夹；
left_only：#只在左边文件夹中存在的文件或文件夹；
right_only：#只在右边文件夹中存在的文件或文件夹；
common_dirs：#两边文件夹都存在的子文件夹；
common_files：#两边文件夹都存在的子文件；
common_funny：#两边文件夹都存在的子文件夹；
same_files：#匹配的文件；
diff_files：#不匹配的文件；
funny_files：#两边文件夹中都存在，但无法比较的文件；
subdirs：#将common_dirs 目录映射到新的dircmp对象，格式为字典的类型。

"""
 
from filecmp import dircmp
import sys
 
# 定义全局变量：
number_different_files = 0    # 文件名相同但不一致的文件数
number_left_only = 0    # 左边目录独有的文件或目录数
number_right_only = 0   # 右边目录独有的文件或目录数
 
 
def print_diff(dcmp):
    """递归比对两目录，如果有不同之处，打印出来，同时累加统计计数。

     1)递归比对两个目录及其所有子目录。2）仅输出两目录不同之处，包括文件名相同(common_files)
     但是文件不一致(diff_files)，以及左、右目录中独有的文件或子目录

    """
    global number_different_files
    global number_left_only
    global number_right_only

    for name in dcmp.diff_files:
        print("diff_file found: %s/%s" % (dcmp.left, name))
        number_different_files += 1

    for name_left in dcmp.left_only:
        print("left_only found: %s/%s" % (dcmp.left, name_left))
        number_left_only += 1

    for name_right in dcmp.right_only:
        print("right_only found: %s/%s" % (dcmp.right, name_right))
        number_right_only += 1

    for sub_dcmp in dcmp.subdirs.values():
        print_diff(sub_dcmp)    # 递归比较子目录
 
 
if __name__ == '__main__':
    try:
        mydcmp = dircmp(sys.argv[1], sys.argv[2])
    except IndexError as ie:
        print(ie)
        print("使用方法：python compare_dir_cn.py 目录1 目录2")
        
    else:
        print("\n比对结果详情: ")
        print_diff(mydcmp)
        if (number_different_files == 0 and number_left_only == 0 
            and number_right_only == 0):
            print("\n两个目录完全一致!")
        else:
            print("\n比对结果统计:")

            print("Total Number of different files is:  %s" 
                %number_different_files)
                  

            print("Total Number of files or directories only in %s is: %s" 
                %(sys.argv[1],number_left_only))
                  
            print("Total Number of files or directories only in  %s is: %s" 
                %(sys.argv[2],number_right_only))
                 
"""
(env375) wuchunlongdeMacBook-Pro:difflib wuchunlong$ python compare_dir_cn.py dir1 dir2

比对结果详情: 
diff_file found: dir1/.DS_Store
diff_file found: dir1/f2.txt
diff_file found: dir1/f3.txt
right_only found: dir2/creat_file1.txt
right_only found: dir2/f5.txt

比对结果统计:
Total Number of different files is:  3
Total Number of files or directories only in 'dir1' is:  0
Total Number of files or directories only in 'dir2' is:  2

"""