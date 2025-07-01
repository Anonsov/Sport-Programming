m = 6
n = 6
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(i)
    matrix.append(row)

# for i in matrix:
#     print(*i)
nmatrix = []
for i in range(m):
    row = []
    for j in range(n):
        if j % 2 == 0:
            row.append(matrix[i][j])
        else:
            row.append(matrix[m-i-1][j])
    nmatrix.append(row)

for i in nmatrix:
    print(*i)    
    
            