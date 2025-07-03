from random import randint
m = 6
n = 5
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(m):
        x+=1
        row.append(randint(0, 100))
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()


for i in range(m//2):
    l = i + 1
    r = m - i - 1
    for j in range(l,  r):
        matrix[i][j] = 0
        

for row in matrix:
    print(*row)
    
    
    