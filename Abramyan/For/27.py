x = 2
n = 3
result = 0

for i in range(1, 2*n, 2):
    v1 = 1
    v2 = 1
    for j in range(1, i, 2):
        v1 *= j
    for k in range(2, i + 1, 2):
        v2 *= k
    result += v1*(x**(i))/v2*i
    
print(result)