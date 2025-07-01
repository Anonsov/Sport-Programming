n = 4
m = 4
k = 4
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i)
        
    matrix.append(row)
print(matrix[k-1])
