from math import sqrt
a = [(1,3), (1,4), (0,2), (3,9)]
b = (0,1)
min = float('inf')
for i in range(0,len(a)):
    x, y = a[i][0], a[i][1]
    xb, yb = b[0], b[1]
    result = sqrt((x-xb)**2 + (y-yb)**2)
    if min > result:
        min = result

print(max)