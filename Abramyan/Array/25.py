n = [-1,3,-4,3,-7,8,-3]
found = False
for i in range(0, len(n) - 1):
    if (n[i] < 0) == (n[i + 1] < 0):
        found = True
        break


print(found)