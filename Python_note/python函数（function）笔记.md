### python函数（function）笔记

#### 函数def：

- 在Python中，定义一个函数要使用 def 语句，依次写出**函数名、括号、括号中的参数和冒号:**，然后，在缩进块中编写函数体，函数的返回值用 **return** 语句返回。

**案例：**


```python
#请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。
#高端写法一：
#在return返回时，进行sum求和，通过for语句进行判断，取出函数的值为X，进行X*X ,最后通过sum（）方法求和

def square_of_sum(L):
    return sum(x*x for x in L)

print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])


#普通写法：
#设定sum“求和值”为O
#再通过for语句进行判断，取出函数的X值，然后X*x求出元素的平方数，在传给sum求和，最后通过return（返回）sum的值
def square_of_sum(L):
    sum=0
    for x in L:
        sum=sum+x*x

    return sum

print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])
```

***

#### 引用包的方法

- 在头部写**import** xxx

***

#### 返回多值的方法

```python
# x = (-b±√(b²-4ac)) / 2a
import math
# sqrt()方法，求X的平方根 link:http://www.runoob.com/python/func-number-sqrt.html
def quadratic_equation(a, b, c):
    t=math.sqrt(b * b - 4 * a * c)
    return (-b + t)/(2 * a), (-b - t)/(2 * a)

    
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

```

***

#### 递归函数：

- 参考

```python
#阶乘运算 n!=n*(n-1)!
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
```

***

#### 定义可变参数：

- 可变参数的名字前面有个 *** **号，我们可以传入0个、1个或多个参数给可变参数：


```python
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
```

***

#### 对列表(list)进行切片

```python
L = range(1,101)
# L设置范围1~100*（range的范围值不包括最后，即(X,N-1）
print L[0:10]
# python程序，读数从0开始，0代表数字的1 
# 输出:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print L[2::3]
# python程序，读数从0开始，2代表数字的3。L[2::3]意思：从数字3开始到结束，每隔3个数字，输出一次 
print L[4:100:5]
print L
```

***

####对列表（list）进行倒序切片

```python
L = range(1,101)
# L设置范围1~100*（range的范围值不包括最后，即(X,N-1）
print L[-10:]
#1~100的范围内，倒数第十个数开始数起
#输出结果;[91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print L[-46:100:5]

```

***

#### 字符串 小写变大写的方法：

```python
#字符串有个方法 upper() 可以把字符变成大写字母：
'abc'.upper()
'ABC'
```

***

#### 索引迭代

- 使用 enumerate() 函数,可以在for循环中同时绑定索引index和元素name

```python
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index, '-', name
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
0 - Adam
1 - Lisa
2 - Bart
3 - Paul
______________________________
# 实际是通过enumerate()函数，变成：
[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
______________________________
#zip()函数可以把两个 list 变成一个 list：
zip([10, 20, 30], ['A', 'B', 'C'])
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[(10, 'A'), (20, 'B'), (30, 'C')]
```

***

#### 复杂表达式

```python
d={'Adam':95,'Lisa':85,'Bart':59}
# 定义字典
def generate_te(name,score): #定义函数
	if score<60: #如果成绩低于60分
		return '<tr><td>%s</td><td style="color:red">%s</td></tr>'% (name,score) 
    #<tr></tr>(表示行)<td></td>(表示列)通过style定义红色是低于60分的

	return '<tr><td>%s</td><td>%s</td></tr>'% (name,score)

tds=[generate_te(name,score)for name,score in d.iteritems()] 
#通过iteritems()方法，解出字典的key和value
print '<table border=1>'
print '<tr><th>name</th><th>score</th></tr>'
print '\n'.join(tds)
print '</table>'

```
- 输出结果

| name | score  |
| ---- | ------ |
| Lisa | 85     |
| Adam | 95     |
| Bart | 59(红色) |

***

#### 条件过滤

- 请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。

```python

def toUppers(L):
	return[x.upper()for x in L if isinstance(x,str)]
# def定义函数toUppers，用return返回
# isinstance(x, str) 可以判断变量 x 是否是字符串；
# 字符串的 upper() 方法可以返回大写的字母。
print toUppers(['Hello','world',101])
```

