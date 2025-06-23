a = [1,1,2,2,2,3,3,4,4,4,4,4,4]
b = []
c = []
bx = 1
first = a[0]
for i in range(1, len(a)):
    if a[i] == first:
        bx += 1
    else:
        b.append(bx)
        c.append(first)
        first = a[i]
        bx = 1
b.append(bx)
c.append(first)
print(b, c)
