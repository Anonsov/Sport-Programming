from random import randint
m = 5
n = 5
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(n):
        x+=1
        row.append(randint(0, 100))
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()

for d in range(m - 1):
    i = m - 1 - d
    j = 0
    while i < m and j < m:
        matrix[i][j] = 0
        i+=1
        j += 1

for i in range(m):
    print(*matrix[i])