n = 2
a1 = 1
a2 = 1
digit = 1
while a2 <= n:
    a1, a2 = a2, a1 + a2
    digit += 1
print(digit)