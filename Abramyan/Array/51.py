a = [4, 23, 5, 35]
b = [15, 31, 5, 35]

for i in range(len(a)):
    a[i], b[i] = b[i], a[i]
print(a, b)
