# -*- coding: utf-8 -*-

# list 列表用[]
L= ['Adam',95.5, 'Lisa',85, 'Bart',59]
print L

#if语句
score = 55
if score>=60:
	print 'Barde 同学的分数是', score
else:
    print 'no pass'


#if elif语句，当多个if语句判断时使用if..elif...else语句
score= 85
if score>=90:
    print 'excellent'
elif score>=80:
    print 'good'
elif score>=60:
    print 'passed'
else:
	print 'failed'


#for语句，用语读取列表（list）和元组（tuple）的有序集合
L= [75, 92, 59, 68]
sum=0.0
for tongx in L:
	sum= sum+tongx
	print sum
print sum/4

# while 和for语句不同 它不会列出序列，只会按条件判断
sum=0
x=1
while x<100:
	sum=sum+x
	x=x+2
	
print sum

#break语句，当条件不满足继续下去时，运行break结束
sum=0
x=1
n=1
while True:
    sum=sum+x
    x=2*x
    n=n+1
    if n>20:
    	break

print sum

#在循环过程中，可以用break退出当前循环，还可以用continue跳过后续循环代码，继续下一次循环。
sum=0
x=0
while True:
	x=x+1
	if x>100:
		break
	if x%2==0:
		continue
	sum=sum+x
print sum

#在循环内部，还可以嵌套循环
for x in range(1,10):
    for y in xrange(10):
    	if x<y:
    		print '%s%s' % (x,y)


#dict 字典的方法用{}
d={
	'Adam': 95,
	'Lisa': 85,
	'Bart': 59,
}

d['Paul']=75

#在字典中插入值的方法

print d


# 在字典里，通过get（）函数可以查找字典的KEY是否存在
d={
	'Adam':95,
	'Lisa':85,
	'Bart':59
}

print 'Adam:',d.get('Adam')
print 'Lisa:',d.get('Lisa')
print 'Bart:',d.get('Bart')


d = {

    'zhangsan' : 99,

    'lisi' : 88,

    'wangwu' : 77,

}

str=input("请输入分数 \n")

for i in d:

    if d[i] == str:

       print i



