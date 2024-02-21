Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 2,3,6,5,4,5,6
type(a)
<class 'tuple'>
b = (56,1,6,59,4)
type(b)
<class 'tuple'>
b[0]
56
b[3]
59
b[3] = 96
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b[3] = 96
TypeError: 'tuple' object does not support item assignment
b.append(65)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b.append(65)
AttributeError: 'tuple' object has no attribute 'append'
a + b
(2, 3, 6, 5, 4, 5, 6, 56, 1, 6, 59, 4)
a
(2, 3, 6, 5, 4, 5, 6)
b
(56, 1, 6, 59, 4)
list(a)
[2, 3, 6, 5, 4, 5, 6]
temp = list(a)
type(temp)
<class 'list'>
temp
[2, 3, 6, 5, 4, 5, 6]
temp[0] = 100
temp
[100, 3, 6, 5, 4, 5, 6]
temp.insert(3,96)
temp
[100, 3, 6, 96, 5, 4, 5, 6]
a = tuple(temp)
a
(100, 3, 6, 96, 5, 4, 5, 6)
x = 56
y = 65
x,y = y,x
x
65
y
56
x,y
(65, 56)
y,x
(56, 65)
a = a+b
a
(100, 3, 6, 96, 5, 4, 5, 6, 56, 1, 6, 59, 4)
a = 2,2,2,2,3,2
for i in range(len(a)):
    if a[i] != a[i+1]:
        print("Elements are not same..")
        break

Elements are not same..
>>> a = 2,2,2,2,2,2
>>> for i in range(len(a)):
...     if a[i] == a[i+1]:
...         print("Elements are same..")
...         break
... 
Elements are same..
>>> a,b,c,d = 56,23,12,45
>>> a
56
>>> c
12
>>> a = {2,365,86,2,2,3,4}
>>> type(a)
<class 'set'>
>>> a
{2, 3, 4, 86, 365}
>>> a = {}
>>> type(a)
<class 'dict'>
>>> b = set()
>>> b
set()
>>> u = {"name":"Ram","Age":65}
>>> u
{'name': 'Ram', 'Age': 65}
