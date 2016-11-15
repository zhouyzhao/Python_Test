### python 字典的笔记

#### dict:

- 字典（dict）用的符号{}

- 字典（dict）有key和value组成 他们的表达方式是 {key：value}

- 本来的字典里没有key和value时，需要插key

  可以输入X[key]=value来插值

代码示例：

```python
d={
    95:'Adam',
	85:'Lisa',
	59:'Bart'
}

d[72]='Paul'

print d
```

***

#### 遍历字典或者列表内容的方法：

- items()

  ```python
  d={
  	'Adam':95,
  	'Lisa':85,
  	'Bart':59
  }

  for x,y in d.items():
  	print '%s:%s' % (x,y)
  ```

***

#### set

- set可以用数学中集合的三要素来记忆：确定性，唯一性，无序性
- set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。

```python
s=set(['Adam','Lisa','Bart','Paul'])
print s

#输出结果：set(['Lisa', 'Paul', 'Adam', 'Bart'])

```

***

#### lower方法

- lower（）方法转换字符串中所有大写字符为小写

```python
s=set([name.lower() for name in ['Adam','Lisa','Bart','Paul']])

print 'adam' in s
print 'bart' in s

#输出结果：
True
False
```

