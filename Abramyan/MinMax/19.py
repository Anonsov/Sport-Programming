n = 6
cnt = 1
min = float('inf')
for i in range(0, n):
    a = int(input())
    if a < min:
        min = a
        cnt = 1
    elif a == min:
        cnt += 1

print(cnt)