b = 3
c = 10
k = 0
cnt = 0
max = float('-inf')
for i in range(0, 5):
    a= int(input())
    if (a > b and a < c) and a > max:
        max = a
        k = i + 1
        cnt += 1

if cnt == 0:
    print(0)
    print(0)
else:
    print(max, k)
    