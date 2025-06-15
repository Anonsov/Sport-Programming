n = 4
max = float('-inf')
for i in range(0, n):
    a = int(input())
    b = int(input())
    if a*b > max:
        max = a*b

print(max)