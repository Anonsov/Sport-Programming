n = 5
summ = 0
min = float('inf')
max = float('-inf')

for i in range(0, n):
    a = int(input())
    summ += a
    if a < min:
        min = a
    if a > max:
        max = a
    
print((summ - min - max)/(n-2))

