from random import randint
m = 3
x = 0
matrix = []
for i in range(m):
    row = []
    for j in range(m):
        # row.append(randint(1, 9))
        x += 1
        row.append(x)
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()

# for i in range((m // 2) + 1):
#     for j in range(m):
#         matrix[i][j], matrix[m-i-1][m-j-1] = matrix[m-1-i][m-1-j], matrix[i][j]

for i in range(m):
    for j in range(m):
        if i * m + j < (m * m) // 2:
            # Меняем элементы на противоположные
            matrix[i][j], matrix[m-1-i][m-1-j] = matrix[m-1-i][m-1-j], matrix[i][j]
# пон
for i in matrix:
    print(*i)
    
print()