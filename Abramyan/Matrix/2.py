m = 3
n = 5
matrix = []

for i in range(1,m+1):
    row = []
    for j in range(1,n+1):
        row.append(5*j)
    matrix.append(row)
for i in matrix:
    print(i)