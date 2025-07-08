from random import randint
m = 9
matrix = []
for i in range(m):
    row = []
    for j in range(m):
        row.append(randint(1, 9))
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()

for d in range(0, (m // 2) + 1):
    for j in range(m - d - 1, d - 1, - 1):
        i = m - d - 1
        matrix[i][j] = 0

  

for i in matrix:
    print(*i)      
        