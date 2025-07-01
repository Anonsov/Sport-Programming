from random import randint
m = 5
n = 6
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

for i in range(m):
    minimum = float('inf')
    min_ind = 0
    max_ind = 0
    maximum = float('-inf')
    for j in range(n):
        s = matrix[i][j]
        if minimum > s:
            minimum = s
            min_ind = j
        elif maximum < s:
            maximum = s
            max_ind = j
    matrix[i][min_ind], matrix[i][max_ind] = matrix[i][max_ind], matrix[i][min_ind]

for i in matrix:
    print(*i)