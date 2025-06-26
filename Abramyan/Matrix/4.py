m = 3
n = 4
matrix = []
for i in range(m):
    row = [i for i in range(1, n+1)]
    matrix.append(row)
for i in matrix:
    print(i)