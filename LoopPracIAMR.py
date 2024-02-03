import math
n = int(input("enter the range.."))
'''sums = 0
for i in range(2,n,2):
    sums += i
print(sums)'''

'''for i in range(1,n+1):
    print(i**3)'''
'''for i in range(1,n):
    print(int(math.pow(i,3)))'''
'''rem = 0
rev = 0
while n > 0:
    rem = n%10
    rev = rev*10 + rem
    n //= 10
    
print(rev)'''

for i in range(2,n//2):
    if n%i == 0:
        print("not a prime..")
        break
else:
    print("number is prime..")
