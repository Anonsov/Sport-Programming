n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    
flag =True
for i in range(n):
    for j in range(n - i - 1):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break
for i in range(n):
    if matrix[i][i] == 1:
        flag = False
        break

if flag or n <= 1:
    print("YES")
else:
    print("NO")