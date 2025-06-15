x = 2
n = 2
result = 0
sign = 1

for i in range(1, n + 1):
    result += sign * ((x**i)/i)
    sign *= -1
    
print(result)