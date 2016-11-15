# -*- coding: utf-8 -*-

# format_string.py

my_name = 'zhou'
my_age = 35 # not a lie
# 将浮点数四舍五入的方法：使用round（）函数
my_height = round(74 * 2.54) # inches(英寸) --> cm（厘米）
my_weight = 180 # 1bs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# %（python字符串格式化）的方法技巧，参考笔记：%c %d %s %r......
print "Let's talk about %s." % my_name
print "He's %r inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
 # this line is tricky, try to get it exactly right
 
print "If I add %d, %d, and %d I get %d."  %(my_age, my_height, my_weight, my_age + my_height + my_weight)
 
