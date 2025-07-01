from random import randint
m = 5
n = 5
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(n):
        x+=1
        row.append(randint(0, 9))
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()

for i in range(m-1):
    for j in range(m-i-1):
        matrix[i][j] = 0

for i in matrix:
    print(*i)