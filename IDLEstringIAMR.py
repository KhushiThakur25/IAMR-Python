Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = "kjsdhfksdjhf"
type(st)
<class 'str'>
st = "212235446"
type(st)
<class 'str'>
st = "Hello world"
len(st)
11
st[5]
' '
st[3]
'l'
st[3] = "m"
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    st[3] = "m"
TypeError: 'str' object does not support item assignment
st[10] = "m"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    st[10] = "m"
TypeError: 'str' object does not support item assignment
st[5] = "m"
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    st[5] = "m"
TypeError: 'str' object does not support item assignment
>>> st.lower()
'hello world'
>>> st.upper()
'HELLO WORLD'
>>> st.capitalize()
'Hello world'
>>> st.title()
'Hello World'
>>> "hello" == "Hello"
False
>>> "hello".casefold() == "Hello".casefold()
True
>>> st
'Hello world'
>>> st.islower()
False
>>> st.isupper()
False
>>> a = "hello"
>>> b = "world"
>>> a+b
'helloworld'
>>> a = "hello "
>>> b = " world"
>>> a+b
'hello  world'
st.swapcase()
'hELLO WORLD'
st = "masses"
st.count("s")
3
st.index("s")
2
st.rindex("s")
5
st.index("z")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    st.index("z")
ValueError: substring not found
st.find("z")
-1
st = "    jksdfhjkdghf dfgfbgf    "
st.strip()
'jksdfhjkdghf dfgfbgf'
st.lstrip()
'jksdfhjkdghf dfgfbgf    '
st.rstrip()
'    jksdfhjkdghf dfgfbgf'
st = "*****jksdfhjkdghf dfgfbgf    "
st.lstrip("*")
'jksdfhjkdghf dfgfbgf    '
st = "jksdfh jkdghf dfgfbgf"
st.split()
['jksdfh', 'jkdghf', 'dfgfbgf']
st.partition("h")
('jksdf', 'h', ' jkdghf dfgfbgf')
st.replace("f","q")
'jksdqh jkdghq dqgqbgq'
st.replace("f","q",3)
'jksdqh jkdghq dqgfbgf'
st.startswith("jks")
True
st.startswith("ks")
False
st.endswith("bg")
False
st = "This is a python programming language"
st = st.split()
st
['This', 'is', 'a', 'python', 'programming', 'language']
" ".join(st)
'This is a python programming language'
"-".join(st)
'This-is-a-python-programming-language'
