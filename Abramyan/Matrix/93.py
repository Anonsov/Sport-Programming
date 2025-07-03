from random import randint
m = 6
n = 5
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(m):
        x+=1
        row.append(randint(10, 99))
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()

