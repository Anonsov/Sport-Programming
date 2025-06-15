n = 5
result = 0
for i in range(1, n+1):
    c = 1
    for j in range(1, i+1):
        c *= j
    result += c
print(result)