n = 4
m = 4
k = 4
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i)
    
    if k == i+1:
        print(row)
        break