n = 5
k = 0
min = float('inf')

for i in range(0, n):
    a = int(input())
    if a < min:
        min = a
        k = i+1
print(k)