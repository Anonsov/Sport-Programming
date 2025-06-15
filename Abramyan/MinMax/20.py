n = 6
cnt_max = 1
cnt_min = 1
min = float('inf')
max = float('-inf')
for i in range(0, n):
    a = int(input())
    if a < min:
        min = a
        cnt_min = 1
    elif a > max:
        max = a
        cnt_max = 1
    elif a == min:
        cnt_min += 1
    elif a == max:
        cnt_max += 1

print(cnt_max, cnt_min, cnt_min + cnt_max)