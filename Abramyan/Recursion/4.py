cnt = 0
def fib1(n):
    global cnt
    if n <= 1:
        cnt += 1
        print(cnt)
        return n
    cnt += 1
    print(cnt)
    a = fib1(n-1)
    b = fib1(n-2)
    return a + b

print(fib1(5))