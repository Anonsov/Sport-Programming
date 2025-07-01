from random import randint
m = 5
n = 5
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(n):
        x+=1
        row.append(randint(0, 100))
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()


for d in range(2*m-1):
    s = 0
    cnt = 0
    for i in range(m):
        j = d - i
        
        if 0 <= j < m:
            s += matrix[i][j]
            cnt += 1
    print(s/cnt)
            