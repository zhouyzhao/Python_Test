# -*- coding: utf-8 -*-
# ex33.py

i = 0
number=10
numbers = []
while i < number:
	print "At the top i is %d " % i
	numbers.append(i)

	i= i+1
	print "Numbers now:", numbers
	print "At the bottom i is %d" %i

print "The numbers:"

for num in numbers:
	print num