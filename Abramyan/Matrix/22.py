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
   
i = 1
while i < n:
    s = 0 
    for j in range(m):
        s += matrix[j][i]
        print(matrix[j][i], end=" ")
    print(s)
    i+=2