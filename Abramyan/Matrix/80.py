from random import randint
m = 5
n = 5
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(n):
        x+=1
        row.append(randint(0, 10))
    matrix.append(row)

for i in matrix:
    print(*i)

print()

s = 0

a = []
for d in range(2 * m - 1):
    if d < m:
        i = 0
        j = m - d - 1
    else:
        i = d - (m - 1)
        j = 0
    
    while i < m and j < m:
        if d == 4:
            break
        print(matrix[i][j], end=" ")
        i += 1
        j += 1
    print("-------")
        
    
    # print(matrix[i-5][i])
    # print(i, "i")