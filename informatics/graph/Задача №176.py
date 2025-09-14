ints = lambda: list(map(int,input().split()))

matrix = []
n = int(input())
for i in range(n):
    row = ints()
    matrix.append(row)
    
    
b = input()    
a = ints()

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] == 1 and a[i] != a[j]:
            cnt += 1


print(cnt // 2)