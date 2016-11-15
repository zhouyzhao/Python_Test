# -*- coding:utf-8 -*-

#在dict字典里插值：d[72]='Paul'
d={
	95:'Adam',
	85:'Lisa',
	59:'Bart'
}

d[72]='Paul'

print d

#使用items（）可以遍历字典或者列表的内容
#在输出时，X[]可以读取字典的key和value
d={
	'Adam':95,
	'Lisa':85,
	'Bart':59
}

for v in d:
	print v+':', d[v] 

#for x,y in d.items():
	#print '%s:%s' % (x,y)


#set可以用数学中集合的三要素来记忆：确定性，唯一性，无序性
#set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
s=set(['Adam','Lisa','Bart','Paul'])
print s

#lower（）方法转换字符串中所有大写字符为小写
# 首先用lower（）方法使得name的字符变成小写，然后用for语句进行判断
s=set([name.lower() for name in ['Adam','Lisa','Bart','Paul']])

print 'adam' in s
print 'bart' in s


#list里对象为tuple类型，通过x[0]、x[1]来进行取值
s= set([('Adam', 95),('Lisa', 85),('bart', 59)])

for x in s:
	print x[0]+':',x[1]






#更新 Set的内容
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print s

def sp():



