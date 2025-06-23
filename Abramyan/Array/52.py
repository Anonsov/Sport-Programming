a = [32.5,5,1,3,5,1,2,6,13]
b = [None] * len(a)

for i in range(0, len(a)):
    if a[i] < 5:
        b[i] = a[i] * 2
    else:
        b[i] = a[i] / 2
    
print(b)