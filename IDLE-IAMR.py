Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = {2,3,5,6,3,2,12,2,3,3}
type(st)
<class 'set'>
st
{2, 3, 5, 6, 12}
a = set()
a
set()
h = {}
type(h)
<class 'dict'>
set_1 = {1,2,3,4,5,6}
set_2 = {4,5,6,7,8,9}
set_1.union(set_2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
set_1
{1, 2, 3, 4, 5, 6}
set_1.update(set_2)
set_1
{1, 2, 3, 4, 5, 6, 7, 8, 9}
set_1 = {1,2,3,4,5,6}
set_1.intersection(set_2)
{4, 5, 6}
set_1.intersection_update(set_2)
set_1
{4, 5, 6}
set_3 = set_1.intersection(set_2)
set_3
{4, 5, 6}
set_1 - set_2
set()
set_1
{4, 5, 6}
set_1 = {1,2,3,4,5,6}
set_1 - set_2
{1, 2, 3}
set_1 = {1,2,3,4,5,6}
set_1.difference(set_2)
{1, 2, 3}
set_1.difference_update(set_2)
set_1
{1, 2, 3}
set_1 = {1,2,3,4,5,6}
set_2 = {4,5,6,7,8,9}
set_1.issubset(set_2)
False
set_2 = {4,5,6}
set_2.issubset(set_1)
True
set_1.issuperset(set_2)
True
set_1.isdisjoint(set_2)
False
set_2.clear()
set_2
set()
del set_2
set_2
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    set_2
NameError: name 'set_2' is not defined. Did you mean: 'set_1'?
>>> set_1.add(23)
>>> set_1
{1, 2, 3, 4, 5, 6, 23}
>>> set_1.remove(3)
>>> set_1
{1, 2, 4, 5, 6, 23}
>>> set_1.remove(65)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    set_1.remove(65)
KeyError: 65
>>> set_1.discard(4)
>>> set_1
{1, 2, 5, 6, 23}
>>> set_1.discard(65)
>>> set_1
{1, 2, 5, 6, 23}
>>> di = {"name","Ram"}
>>> type(di)
<class 'set'>
>>> dic = {"name":["Ram","Dev","Vaishali","Amit","Aman","Yash","Sevy"],"age":[55,21,1945,26,25,26],"dept":["IT","INTERN","INTERN","CEO","EMPLOYEE","TRAINER","TRAINER"]}
>>> dic["age"][1]
21
