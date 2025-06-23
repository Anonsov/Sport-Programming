n = [3,6,9,11,15]
b = n[1] - n[0]
isProgress = True
for i in range(0, len(n) - 1):
    if n[i + 1] - n[i] != b:
        isProgress = False
        break
if isProgress:
    print(b)
else:
    print(0)

