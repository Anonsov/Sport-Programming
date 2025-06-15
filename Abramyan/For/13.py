n = 3
sign = 1
c = 0

for i in range(11, n + 11):
    c += (sign * i/10)
    sign *= -1
    
print(c)