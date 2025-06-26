a = [1,2,1,3,3,3,5,5,6]
i = 1
while i < len(a):
    if a[i] != a[i-1]:
        a.insert(i, 0)
        i+=1
    i+=1
a.append(0)
print(a)