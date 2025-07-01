m = 9
n = 8
matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(i)
    matrix.append(row)

for i in matrix:
    print(*i)

# print(print() ==)
for i in range(m):
    for j in range(m-i):
        print(matrix[j][i], end=" ")
    for j in range(i+1,m):
        print(matrix[m-i-1][j], end=" ")
# x = 0
# for i in range(m):
#     if i % 2 == 0:
#         print(matrix[x])
#         x+=1
#     else:
#         print(matrix[m-x]) 
    


    
# print()
# x = 0
# while x < m:
#     if x % 2 == 0:
#         print(matrix[x])
#     else:
#         
# print(matrix[m-x])
#     x+=1



