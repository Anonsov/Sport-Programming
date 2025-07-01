from random import randint
m = 5
n = 6
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(n):
        x+=1
        row.append(randint(1, 10))
    matrix.append(row)

for i in matrix:
    print(*i)

print()

i = 0
k = 0
minimum = float('inf')
while i < n:
    s = 1
    for j in range(m):
        s *= matrix[j][i]
    if minimum > s:
        minimum = s
        k = i
    i += 1
print(minimum, k)