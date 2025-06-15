n = 4
d = n
c = 0

for i in range(1, n+1):
    
    c += i ** d
    d -= 1
print(c)