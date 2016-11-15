# -*- coding:utf-8 -*-


"""
问题：sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
解答：L是列表
通过for语句进行范围range（）读取
读取的结果会返回到L的列表中，再通过sum（）函数进行求和

"""
L=[]
for x in range(1,101):
	L.append(x*x)

print sum(L)

"""
解答：L是列表
先设定X值为1
通过while函数进行判断 通过append()方法进行追加到L列表中
通过x+1进行x值的叠加
最后通过sum（）函数进行求和

"""
L = []
x = 1
while x <= 100:
	L.append( x * x )
	x = x+1

print sum(L)



#请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。


def square_of_sum(L):
    return sum(x*x for x in L)

    


print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])


def square_of_sum(L):
    sum=0
    for x in L:
        sum=sum+x*x

    return sum

print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])



# x = (-b±√(b²-4ac)) / 2a
import math
# sqrt()方法，求X的平方根 link:http://www.runoob.com/python/func-number-sqrt.html
def quadratic_equation(a, b, c):
    t=math.sqrt(b * b - 4 * a * c)
    return (-b + t)/(2 * a), (-b - t)/(2 * a)

    
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)



#阶乘运算 n！=n*(n-1)!
"""
阶乘运算的参考：
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
"""

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
    

print fact(5)



#模拟汉诺塔逻辑，
def move(n,a,b,c):
    if n==1:
        print a,'-->',c
        return
    move(n-1,a,c,b)
    print a,'-->',c
    move(n-1,b,a,c)

move(4,"A","B","C")


#默认函数，当def定义了函数参数，下面的函数没参数时，直接调用默认函数参数，如果下面的函数具有参数时，则使用下面的参数内容
def greet(name='world'):
    print "Hello "+ name + ""

greet()
greet('Bart')


def average(*args):
    sum=0.0
    if len(args)==0:
        return sum
    for x in args:
        sum=sum+x
    return sum/len(args)

print average()
print average(1,2)
print average(1,2,2,3,4)