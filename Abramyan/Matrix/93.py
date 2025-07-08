from random import randint
m = 8
n = 5
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(m):
        x+=1
        row.append(randint(1, 9))
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()
# cnt = m
# for d in range((m // 2) + 1):
#     i = d + 1
#     j = m - d - 1
#     while i < m - 1 and i < cnt:
#         matrix[i][j] = 0
#         i += 1

for d in range(1, (m // 2) + 1):
    for  i in range(d , m -d ):
        j = m - d 
        matrix[i][j] = 0 


    # cnt -= 2
for i in matrix:
    print(*i)
    