Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = "Hello wolrd"
st[0]
'H'
>>> st[0:4]
'Hell'
>>> st[0:5]
'Hello'
>>> st[0:6:2]
'Hlo'
>>> st[5:0:-1]
' olle'
>>> st[5:-1:-1]
''
>>> st[-10]
'e'
>>> st[-11]
'H'
>>> st[len(st)-1:-11:-1]
'drlow olle'
>>> st[len(st)-1:-12:-1]
'drlow olleH'
>>> st[len(st)-1:-12:1]
''
>>> st[]
SyntaxError: incomplete input
>>> st[:]
'Hello wolrd'
>>> st[::-1]
'drlow olleH'
