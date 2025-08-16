def combin1(n, k):
    global cnt
    cnt += 1
    
    if k == 0 or n == k:
        return 1
    
    return combin1(n-1, k) + combin1(n-1, k-1)

cnt = 0
result = combin1(4, 2)
print(f"C(4, 2) = {result}, вызовов: {cnt}")