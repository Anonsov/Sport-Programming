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
    
for i in range(m):
    if i % 2 == 0:
        print(matrix[i][::-1])
    else:
        print(matrix[i])
