Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = list()
>>> type(a)
<class 'list'>
>>> a
[]
>>> a.append(2)
>>> a
[2]
>>> b = [3,5,6,8,9,1]
>>> b.append(65)
>>> b
[3, 5, 6, 8, 9, 1, 65]
>>> b[2] = 3
>>> b
[3, 5, 3, 8, 9, 1, 65]
>>> b.insert(2,6)
>>> b
[3, 5, 6, 3, 8, 9, 1, 65]
>>> a.append(56,45,87)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append(56,45,87)
TypeError: list.append() takes exactly one argument (3 given)
>>> a.append([56,45,87])
a
[2, [56, 45, 87]]
a.extend([56,45,87])
a
[2, [56, 45, 87], 56, 45, 87]
a[1]
[56, 45, 87]
a[1][1]
45
list_1 = [1,2,3,4,4,5]
list_2 = [5,6,8,9]
list_1.extend(list_2)
list_1
[1, 2, 3, 4, 4, 5, 5, 6, 8, 9]
list_1.pop()
9
list_2.pop(5)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list_2.pop(5)
IndexError: pop index out of range
list_1.pop(5)
5
list_1.remove(4)
list_1
[1, 2, 3, 4, 5, 6, 8]
list_1.remove(8)
list_1
[1, 2, 3, 4, 5, 6]
del list_1
list_1
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list_1
NameError: name 'list_1' is not defined. Did you mean: 'list_2'?
list_1 = [64,21,45,87,91,100]
list_1.sort()
list_1
[21, 45, 64, 87, 91, 100]
list_1 = [64,21,45,87,91,100]
list_1.sort(reversed= True)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    list_1.sort(reversed= True)
TypeError: 'reversed' is an invalid keyword argument for sort()
list_1.sort(reverse = True)
list_1
[100, 91, 87, 64, 45, 21]
list_1 = [64,21,45,87,91,100]
list_1.reverse()
list_1
[100, 91, 87, 45, 21, 64]
list_1 = [1,2,3,4,4,5]
len(list_1)
6
list_1.count(4)
2
list_1.index(4)
3
m = list_1
m
[1, 2, 3, 4, 4, 5]
list_1
[1, 2, 3, 4, 4, 5]
m[0] = 65
m
[65, 2, 3, 4, 4, 5]
list_1
[65, 2, 3, 4, 4, 5]
list_1[2] = 100
list_1
[65, 2, 100, 4, 4, 5]
m
[65, 2, 100, 4, 4, 5]
n = m.copy()
n
[65, 2, 100, 4, 4, 5]
m
[65, 2, 100, 4, 4, 5]
n[0] = 106
n
[106, 2, 100, 4, 4, 5]
m
[65, 2, 100, 4, 4, 5]
m.max()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    m.max()
AttributeError: 'list' object has no attribute 'max'
type(m)
<class 'list'>
m.sum()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    m.sum()
AttributeError: 'list' object has no attribute 'sum'
import sys
sys.getsizeof([])
56
sum(m)
180
max(m)
100
min(m)
2
