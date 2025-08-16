def rootk(x, k, n):
    if n == 0:
        return 1
    yn = rootk(x, k, n - 1)
    yn1 = yn - (yn - (yn - x / (yn ** (k - 1)))) / k
    return yn1

x = 8
k = 3

for n in range(6):
    result = rootk(x, k, n)
    print(f"N = {n}: rootk({x}, {k}, {n}) = {result:.6f}")
