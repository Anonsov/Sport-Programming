cnt = 0
n = 6
min = float('+inf')
cnt_1 = 0
for i in range(0, n):
    a = int(input())
    if a < min:
        min = a
        cnt = i
print(cnt, min)