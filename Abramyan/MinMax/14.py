b = 10
k  = 0
cnt = 0
min = float('inf')

for i in range(0, 10):
    a = int(input())
    if a < min and a > b:
        k= i+1
        cnt += 1
        min = a

if cnt == 0:
    print(0)
    print(0)
else:
    print(min, k)
    