from random import randint
m = 5
n = 6
matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(randint(1,5))
    matrix.append(row)

for i in matrix:
    print(*i)
   
print()


i = 0
k = 0
maximum = float('-inf')

while i < m:
    s = 0
    for j in range(n):
        s += matrix[i][j]
    if maximum < s:
        maximum = s
        k = i   
    i += 1
print(k, s)