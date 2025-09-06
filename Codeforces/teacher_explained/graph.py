# n, m = map(int, input().split())
# g = [[] for i in range(n + 1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     g[v].append(u)
#     g[u].append(v)

# used = [False for _ in range(n + 1)]
# def dfs(v: int):
#     if used[v]:
#         return
#     used[v] = True
#     for i in range(len(g[v])):
#         dfs(g[v][i])
# s = 0
# for i in range(1, n + 1):
#     if not used[i]:
#         s += 1
#         dfs(i)

# if s == 1 and n - m == 1:
#     print("YES")
# else:
#     print("NO")


n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

s = 0
used = [False for _ in range(n + 1)]
def dfs(v: int):
    if used[v]:
        return
    used[v] = True
    s += 1
    for i in g[v]:
        dfs(i)

for i in range(1, n + 1):
    if not used[i]:
        dfs(i)

