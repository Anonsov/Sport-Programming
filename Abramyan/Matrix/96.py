from random import randint
m = 5
matrix = []
for i in range(m):
    row = []
    for j in range(m):
        row.append(randint(1, 9))
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()

for d in range(m - 1):
    i = 0
    j = m - d - 1
    while i < m and j < m:
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        i += 1
        j += 1
        

for i in matrix:
    print(*i)
    