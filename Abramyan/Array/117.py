a = [1,1,2,2,2,2,3,3,4]
res = []

for i in range(0, len(a) - 1):
    if a[i] != a[i+1]:
        res.insert(i-1, 0)
    res.append(a[i])
print(res)