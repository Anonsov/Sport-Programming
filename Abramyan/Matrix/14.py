m = 7
n = 9
matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(j)
    matrix.append(row)

for i in matrix:
    print(*i)
    
# a = [1,2,4,3,5,13, 4]
# x = 0
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[x])
#         x += 1
#     else:
#         print(a[len(a) - x])
print()
for i in range(m):
    x = 0
    row = []
    for j in range(n):
        if j % 2 == 0:
            row.append(matrix[i][x])
            x += 1
        else:
            row.append(matrix[i][n - x])
    print(row)        