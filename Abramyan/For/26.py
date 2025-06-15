x = 4
sign = 1
result = 0
for i in range(1, 2 * x + 1, 2):
    result += sign * ((x**i) / i)
    sign *= -1
    print(result)
print(result )