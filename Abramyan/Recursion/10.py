def digitsum(k):
    if k == 1:
        return 1
    return k + digitsum(k - 1)

print(digitsum(4))