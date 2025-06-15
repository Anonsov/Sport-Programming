a = 8930
i = 0
cnt = 0
while a > 1:
    digits = a % 10
    a //= 10
    i += digits
    cnt += 1
print(i, cnt)