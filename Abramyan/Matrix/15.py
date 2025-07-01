m = 5
n = 5
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(n):
        x+=1
        row.append(x)
    matrix.append(row)

for i in matrix:
    print(*i)
    
    
result = []
for l in range(m // 2):
    start = l
    end = m - 1 - start

    for i in range(start, end + 1):
        result.append(matrix[start][i])
    
    for j in range(start + 1, end + 1):
        result.append(matrix[j][end])
    
    for i in range(end - 1, start - 1, -1):
        result.append(matrix[end][i])
    
    for j in range(end - 1, start, -1):
        result.append(matrix[j][start])
        
c = m//2
result.append(matrix[c][c])   
print(result, len(result))
    