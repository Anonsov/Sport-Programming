primes = "2357"
a = 4869
found = False
while a > 1:
    digits = a % 10
    a //= 10
    if str(digits) in str(primes):
        found = True
        break

if found:
    print(True)
else:
    print(False)         
