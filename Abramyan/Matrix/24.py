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


i = 0
while i < n:
    s = 0
    mx = float('-inf')
    for j in range(m):
        s = matrix[j][i]
        if mx < s:
            mx = s
    print(mx)
    i+=1