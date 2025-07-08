from random import randint
m = 7
matrix = []
for i in range(m):
    row = []
    for j in range(m):
        row.append(randint(1, 9))
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()

for i in range(m):
    for j in range(m - i - 1):
        matrix[i][j], matrix[m - 1 - j][m - 1 - i] = matrix[m - 1 - j][m - 1 - i], matrix[i][j]
    
for i in matrix:
    print(*i)
    