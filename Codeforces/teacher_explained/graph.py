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


# n, m = map(int, input().split())
# g = [[] for _ in range(n+1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)

# s = 0

# used = [False for _ in range(n + 1)]
# def dfs(v: int):
#     if used[v]:
#         return
#     used[v] = True
#     for i in g[v]:
#         dfs(i)

# for i in range(1, n + 1):
#     if not used[i]:
#         s += 1
#         dfs(i)
        
# if m > n - s:
#     print("YES")
# else:
#     print("NO")

# bfs trying 
# from collections import deque

# ints = lambda: map(int, input().split())

# n, m = ints()
# g = [[] for i in range(n + 1)]

# for i in range(m):
#     v, u = ints()
#     g[v].append(u)
#     g[u].append(v)
# s = 0

# used = [False for i in range(n + 1)]

# def bfs(v):
#     q = deque()
#     q.append(v)
#     used[v] = True
#     while q:
#         v = q.popleft()
#         print(f"visiting vertex {v}")
        
#         for i in g[v]:
#             if not used[i]:
#                 used[i] = True
#                 q.append(i)


# for i in range(1, n + 1):
#     if not used[i]:
#         s += 1
#         bfs(i)
    
# print(s)


# dijikastra algorithm tryings
# non-directed graph 
# from collections import deque
# ints = lambda: map(int, input().split())
# n, m = ints()
# g = [[] for i in range(n + 1)]
# for i in range(m):
#     u, v, w = ints()
#     g[u].append((v, w))
#     g[v].append((u, w))

# queue = deque()

# for i in g[2]:
#     queue.append(i)

# print(queue)

# while queue:
#     v = queue.popleft()
#     for i in range(g[v]):

# for i in g:
#     print(i)

# from collections import PriorityQueue(maxsize=0)
from collections import deque
ints = lambda: map(int, input().split())
n, m = ints()
g = [[] for i in range(n + 1)]
for i in range(m):
    u, v, w = ints()
    g[u].append((v, w))
    g[v].append((u, w))
    
for i in g:
    print(i)


dist = [float('inf')] * (n + 1)
prev = [-1] * (n + 1)

s = 1
dist[s] = 0

q = deque([s])

while q:
    v = q.popleft()
    for u, w in g[v]:
        ndist = dist[v] + w
        if ndist < dist[u]:
            dist[u] = ndist
            prev[u] = v
            q.append(u)
                
