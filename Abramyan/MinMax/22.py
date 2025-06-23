n = 5
a1 = float('-inf')
max = float('-inf')
for i in range(0, n):
    a = int(input())
    if a1 + a  >= max:
        max = a1 + a
        a1 = a

print(max)