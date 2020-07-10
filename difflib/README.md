2020.06.14

功能：python3.7.5环境   

diff_file.py     
1、compare_file(file1, file2, out_file) 比较文件内容，并显示
2、file_cmp(file1, file2, shallow) 单文件对比
3、file_cmpfiles(dir1,dir2,lis,shallow=True) 比较两个文件夹内指定文件是否相等


compare_dir_cn.py
递归比对两目录，如果有不同之处，打印出来，同时累加统计计数。
1) 递归比对两个目录及其所有子目录;
2）仅输出两目录不同之处，包括文件名相同(common_files),但是文件不一致(diff_files);
3）以及左、右目录中独有的文件或子目录



