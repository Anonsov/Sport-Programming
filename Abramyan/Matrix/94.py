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

for d in range(1, (m // 2) + 1):
    for i in range(d, m - d):
        j = d - 1
        matrix[i][j] = 0
        
for i in matrix:
    print(*i)
    

