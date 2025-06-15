n = 8
a1 = 1
a2 = 1
digit = 0
prev = 0
next = 0
while a2 <= n:
    prev = a1
    a1, a2 = a2, a1 + a2
    next = prev + a1
print(prev, next)