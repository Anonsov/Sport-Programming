a = 57
b = 9
c = 0

while a % b != 0:
    c = a%b
    a = b
    b = c
if a % b == 0:
    c = b
print(c)