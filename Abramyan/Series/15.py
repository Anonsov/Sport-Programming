k = 5
first = 0
found = False
while True:
    a = int(input())
    if a == 0:
        break
    if a > k and found == False:
        first += 1
        found = True

print(first)