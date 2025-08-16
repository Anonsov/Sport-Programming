def max_elem(a, n):
    if n == 1:
        return a[0]
    return max(a[0], max_elem(a[1:], n - 1))

a = [3, 7, 2, 9, 1, 5]
n = len(a)
print(max_elem(a, n))