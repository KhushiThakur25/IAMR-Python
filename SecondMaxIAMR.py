'''lis = [42,13,28,45,54,47]
maxs = lis[0]
secmax = lis[0]
for i in lis:
    if i > maxs:
        secmax = maxs
        maxs = i
    if i > secmax and maxs > i:
        secmax = i

print("Maximum value is:",maxs)
print("Maximum value is:",secmax)'''

'''lis.remove(maxs)


maxs = lis[0]
for i in lis:
    if i > maxs:
        maxs = i
print("Second Maximum value is:",maxs)'''
        
lis = [[1,3,9],[2,10,12],[3,18,5],[9,5,6,7]]
'''print(len(lis))
print(len(lis[0]))'''
maxs = lis[0][0]
for i in range(len(lis)):
    for j in range(len(lis[0])):
        '''print(lis[i][j],end = "  ")
    print()'''
        if maxs < lis[i][j]:
            maxs = lis[i][j]

print(maxs)
