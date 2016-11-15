# -*- coding: utf-8 -*-

L = range(1, 101)
print L[0:10]
print L[2::3]
print L[4:100:5]
print L
print L[-10:]

print L[-46:100:5]

print '*'*100


def firstCharUpper(s):
    return s[0].upper()+s[1:]
print firstCharUpper("hello")
print firstCharUpper("sunday")
print firstCharUpper("september")

print '*'*100
for i in range(7,101,7):
	print i

print '*'*100
for x in range(1,101):
	if x % 7==0:
		print x

print '*'*100


L=['Adam','Lisa','Bart','Paul']

for index,name in zip(range(1,5),L):

	print index, '-', name

print '*'*100

d={'Adam':95,'Lisa':85,'Bart':59,'Paul':74}

sum = 0.0

for x in d.values():
	sum=sum+x

print sum/4

d={'Adam':95,'Lisa':85,'Bart':59,'Paul':74}

sum=0.0
for k,v in d.iteritems(): #iteritems()获取字典里的key和values的值 
	sum=sum+v
	print k,':',v

print 'average',':',sum/len(d)

#请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print[x*(x+1) for x in range(1,100,2)]

print '*'*100



d={'Adam':95,'Lisa':85,'Bart':59}
# 定义字典
def generate_te(name,score): #定义函数
	if score<60: #如果成绩低于60分
		return '<tr><td>%s</td><td style="color:red">%s</td></tr>'% (name,score) #<tr></tr>(表示行)<td></td>(表示列)通过style定义红色是低于60分的

	return '<tr><td>%s</td><td>%s</td></tr>'% (name,score)

tds=[generate_te(name,score)for name,score in d.iteritems()] #通过iteritems()方法，解出字典的key和value
print '<table border=1>'
print '<tr><th>name</th><th>score</th></tr>'
print '\n'.join(tds)
print '</table>'

print '*'*100




def toUppers(L):
	return[x.upper()for x in L if isinstance(x,str)]
	

print toUppers(['Hello','world',101])

print '*'*100


print[100*n1+10*n2+n3 for n1 in range(1,10) for n2 in range(10) for n3 in range(10) if n1==n3]

