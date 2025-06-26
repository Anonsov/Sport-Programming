m = 4
n = 4
d = 5
matrix = []
for i in range(1, m+1):
    row = []
    for j in range(n):
        row.append(i+j*d)
    matrix.append(row)
    
for j in matrix:
    print(j)