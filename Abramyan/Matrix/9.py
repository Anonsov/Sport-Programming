n = 6
m = 6
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(i+1)
    matrix.append(row)

for i in matrix:
    print(*i)
    
for i in range(2, len(matrix), 2):
    print(matrix[i])