n = 13
a1 = 1
a2 = 1
digit = 0
while a2 < n:
    a1, a2 = a2, a1 + a2
    
if n == a2:
    print(True)
else:
    print(False)  
    