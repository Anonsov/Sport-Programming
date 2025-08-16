def powern(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / powern(x, -n)
    else:
        return x * powern(x, n - 1)


print(powern(1, 0))
print(powern(2, 3))
print(powern(2, -3))
