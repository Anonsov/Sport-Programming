m = 5
n = 6
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(n):
        x+=1
        row.append(x)
    matrix.append(row)

for i in matrix:
    print(*i)
   
for i in range(m):
    s = 0
    for j in range(n):
        s += matrix[i][j]
    print(s)
    