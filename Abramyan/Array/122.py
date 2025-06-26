k = 4
a = [1,1,1,1,2,2,2,2,3,3,4,4]
print(len(a))
i = 1
cnt = 0
length = 1
while i < len(a):
    if a[i] == a[i-1] and len(a) - 1 != i:
        length += 1
    else:
        cnt += 1
        if cnt == k:
            while length >= 1:
                a.pop(i-1)
                length -= 1
                i-=1
        length = 1
        
    i+=1
print(cnt, "cnt")
print(a, len(a))

