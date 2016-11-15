# -*- coding: utf-8 -*-

# ex15.py
# 从代码库sys 输入 argv模块
from sys import argv

# script， filename获得argv的功能
script, filename = argv

# txt打开文件
txt = open (filename)
# 输出文件名
print "Here's your file %r:" % filename
# 从txt中读写内容
print txt.read()

print "Type the filename again:"
# 输raw_import 文件名
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()
print txt_again.close()
