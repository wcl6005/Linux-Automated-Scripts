# -*- coding: UTF-8 -*-

# 字节转换为B、KB、MB、GB、TB。使用 and or 一行语句 解决多分支问题。
def size_Convert(b):
    if isinstance(b,str): #判断b是字符串  重构 2019.02.19
        b = int(b) if b.isdigit() else -1 #所有字符都是数字    
    return b >= 1099511627776 and '%.2f%s' %(round(b/1099511627776.0,2),'TB')\
        or b >= 1073741824 and '%.2f%s' %(round(b/1073741824.0,2),'GB')\
        or b >= 1048576 and '%.2f%s' %(round(b/1048576.0,2),'MB')\
        or b >= 1024 and '%.2f%s' %(round(b/1024.0,2),'KB')\
        or b >= 0 and '%d%s' %(b,'B') or '%s' %('err') 
      
b = '1025935'
print(size_Convert(b))