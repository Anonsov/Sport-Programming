matrix = []
n = 4
m = 4
k = 2
for i in range(n):
    row = []
    for j in range(m):
        row.append(j)
    matrix.append(row)
print(matrix)
for i in range(0, len(matrix)):
    print(matrix[i][k])