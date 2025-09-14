n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
flag = False
for i in range(n):
    if matrix[i][i] == 1:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
        