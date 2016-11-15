# -*- coding: utf-8 -*-
# ex32.py

the_count = [1, 2, 3, 4, 5, 6]
fruits = ['apple', 'otganges', 'peats', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list 
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" %fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't konw what's in it 
for i in change:
	print "I got %r" %i

# we can also build lists, first start with empty one
elements= [100]

# then usr the range function to do 0 to 5 counts
for i in range(0,6):# 使用range函数.函数给定的终点永远不会在生成的列表中
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Elements was: %d " %i

#列表对象测试：

for a in range(len(fruits)):
	print a, fruits[a]


the_count.insert(4,100)
print the_count