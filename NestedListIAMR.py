import math
'''list_1 = [[1,2,3],[4,2,1],[2,10,12]]
maxs = list_1[0][0]
for i in range(len(list_1)):
    for j in range(len(list_1[0])):
        
        if maxs < list_1[i][j]:
            maxs = list_1[i][j]
            
print("Max element is :",maxs)'''
#method 1
list_1 = [[1,2,3],[4,2,1],[2,10,12]]
list_2 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(list_1)):
    k = 0
    for j in list_1[i]:
        
        list_2[i][k] = j**2
        k += 1

print(list_2)
#method 2
list_1 = [[1,2,3],[4,2,1],[2,10,12]]
for i in range(len(list_1)):
    
    for j in range(len(list_1[0])):
        
        list_1[i][j] = list_1[i][j]**2
        
        

print(list_1)
#method 3
list_1 = [[1,2,3],[4,2,1],[2,10,12]]
for i in range(len(list_1)):
    
    for j in range(len(list_1[0])):
        
        list_1[i][j] = int(math.pow(list_1[i][j],2))
        
        

print(list_1)

        
        
            
