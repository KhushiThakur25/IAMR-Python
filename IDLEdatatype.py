Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Python312/ChatAppSP.py
Enter your message..:bye
Bye user
>>> 16<<2
64
>>> 16>>2
4
>>> 20<<2
80
>>> 20>>2
5
>>> a = 5
>>> type(a)
<class 'int'>
>>> a + 1
6
>>> a
5
>>> a = a+1
>>> a
6
>>> st = "hello world"
>>> st[3]
'l'
st[3] = "q"
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    st[3] = "q"
TypeError: 'str' object does not support item assignment
del st[3]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    del st[3]
TypeError: 'str' object doesn't support item deletion
tup = (1,2,3,4)
tup[2]
3
tup[2] = 65
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tup[2] = 65
TypeError: 'tuple' object does not support item assignment
del tup[2]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    del tup[2]
TypeError: 'tuple' object doesn't support item deletion
lists = [65,3,6,5,9,4]
lists[0]
65
lists[0] = 2
lists
[2, 3, 6, 5, 9, 4]
del lists[0]
lists
[3, 6, 5, 9, 4]
