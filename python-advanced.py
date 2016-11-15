# -*- coding:utf-8 -*-

#help ('math')

import math

def add(x,y,f):
	return f(x)+f(y)

print add(25,9,math.sqrt)

print '*'*100
def formate_name(s):
	return s.capitalize()


print map(formate_name,['adam','LISA','barT'])

print '*'*100

def prod(x,y):
	return x*y

print reduce(prod,[2,4,5,7,12])


def calc_prof(list):
    def a(list):
        result = 1
        for i in list:
            result = result * i
        return result
    return a(list)
f = calc_prof([1, 2, 3, 4])

print (f)