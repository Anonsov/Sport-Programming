n = 5
k = 0
max = float('-inf')
for i in range(0, n):
    m = int(input())
    v = int(input())
    if m/v > max:
        k = i + 1
        max = m/v
    
print(k)