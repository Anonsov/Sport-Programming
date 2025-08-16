memo = {}
def fib2(n):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]

print(fib2(5))