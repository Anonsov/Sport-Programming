n = 5
cnt = 0
max = float('-inf')
found = False
for i in range(0, n):
    a = int(input())
    if a > max:
        max = a
        cnt = 0
    elif a == max:
        found = True
    if a != max:
        cnt += 1

if found:
    print(cnt)
else:
    print(0)