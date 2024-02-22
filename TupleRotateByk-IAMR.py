tup = (1,2,3,4,5,6)
print("Tuple before rotate..",tup)
a = list(tup)

k = int(input("Enter the rotating items."))
while k>0:
    k -= 1
    n = a[len(a)-1]
    for i in range(len(a)-1,0,-1):
        a[i] = a[i-1]
    a[0] = n
tup = tuple(a)  
print(tup)
