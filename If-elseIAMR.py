a = 5
b = 6
c = 20
'''
if a>b and a>c:
    print("a is greater..")
elif b>a and b>c:
    print("b is greater..")
else:
    print("c is greater..")'''

#expression for if-else

n = 32
'''if n%2 == 0:
    print("Even number")
else:
    print("Number is odd")'''
result = "Even" if n%2 == 0 else "odd"
print(result,"Number")

res = "a" if a>b and a>c else "b" if b>a and b>c else "c"
print(res,"is greatest..")
