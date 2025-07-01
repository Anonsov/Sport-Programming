m = 6
n = 6
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(j+1)
    matrix.append(row)

for i in matrix:
    print(*i)
    
for i in range(0, m):
    row = []
    for j in range(0, n, 2):
        row.append(matrix[i][j])
    print(row)
    