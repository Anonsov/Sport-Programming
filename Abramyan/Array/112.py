a = [8, 3, 7, 5, 2, 1, 0]

for x in range(0, len(a)):
    for i in range(0, len(a) - x - 1):
        if a[i] > a[i+1]:
            a[i+1], a[i] = a[i], a[i+1]
        print(a)
        
print(a)