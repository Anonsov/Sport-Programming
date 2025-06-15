x = 3
n = 4
result = 0
sign = 1
for i in range(0, 2*n, 2):
    c = 1
    for j in range(1, i + 1):
        c*=j
    result += sign * ((x**i)/c)
    sign *= -1
    
print(result)