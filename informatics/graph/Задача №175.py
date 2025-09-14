ints = lambda: map(int, input().split())

n, m = ints()
g = [[] for _ in range(n + 1)]
for i in range(m):
    v, u = ints()
    g[u].append(v)
    g[v].append(u)


res = []
for i in range(1, n + 1):
    res.append(len(g[i]))


print(*res)