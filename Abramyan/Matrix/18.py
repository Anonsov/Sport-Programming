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
 
 
s = 0
k = 2
for i in range(m):
    s += matrix[i][k-1]  
    print(s)
