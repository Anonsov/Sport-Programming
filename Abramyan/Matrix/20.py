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
   
i = 0
while i < n:
    s = 1
    for j in range(m):
        s *= matrix[j][i]
    print(s)
    i += 1