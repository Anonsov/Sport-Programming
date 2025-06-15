n = 5
k = 0
max = float('-inf')
for i in range(0, n):
    a = int(input())
    if a >= max:
        k = 0
        max = a
    else:
        k+=1
print(k)
