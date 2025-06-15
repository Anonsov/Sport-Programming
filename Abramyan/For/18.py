a = 4
n = 3
c = 0
sign = 1
for i in range(0, n + 1):
    c += sign*(a**i)
    sign*=-1
print(c)
    