a = 1840
found = False
while a > 1:
    digits = a % 10
    a //= 10
    if digits == 2:
        found = True
        break

if found:
    print(True)
else:
    
    print(False)    