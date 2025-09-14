n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

cnt = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            cnt += 1

print(cnt // 2)     