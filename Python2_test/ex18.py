# -*- coding: utf-8 -*-
# ex18.py

# this one is like your scripts with argv

def print_two (*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r " % (arg1, arg2) # 避免出现缩进错误，同时两个缩进的情况下，使用tab代替空格



# ok, that *args is actually pointless, we can just do this 
def print_two_again (arg1, arg2):
    print "arf1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one (arg1):
    print "arg1: %r" % arg1

# this one takes no argement

def print_none ():
    print "I got nothin'."

print_two ("zed","shaw")
print_two_again ("zed", "shaw")
print_one ("First!")
print_none ()
