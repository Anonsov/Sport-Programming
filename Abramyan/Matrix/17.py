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
   
k = 2 
s = 0
for i in range(n):
    s += matrix[k-1][i]
print(s)