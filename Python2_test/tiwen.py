# -*- coding: utf-8 -*-

"""
print "How old are you?",
age = raw_input()
print "How tall are you ?",
height = raw_input()
print "How much do you weigh?",
weigh = raw_input()

print "So,you're %r old, %r tall and %r heavy."% (age, height, weigh)

"""

# 百度 raw_input()的知识练习， 以下是练习1 参考地址：http://blog.sina.com.cn/s/blog_6cbb8d870100o1cn.html
# python 读取输入值操作方法： 输入整数
'''
nAge = int(raw_input ("input your age plz:\n"))
if nAge > 0 and nAge < 120 :
    print "thanks!"
else :
    print "bad age"
    print "your age is %d" % nAge
'''

# 练习2 python 读取输入值操作方法： 输入字符串

nID = '' # nIDw为空
while 1: #while循环语句
    nID = raw_input("Input your id plz: \n") #输入nID的值
    if len(nID) != len("1322***"): #如果nId的值不等于13222***
        print "wring length of id, input again" #输出 "wring length of id, input again"，'your id is %s' % (nID)
    else: #如果nID的值，是13222***，循环结束
        break 
    print 'your id is %s' % (nID)
