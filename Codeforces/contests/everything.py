# # a
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     if n % 4 == 0:
#         print("Bob")
#     else:
#         print("Alice")
        
# t = int(input())

# for _ in range(t):
#     n, j, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     cur = a[j-1]
#     x = 0
#     for i in a:
#         if i > cur:
#             x += 1
    
#     if x <= n - k:
#         print("YES")
#     else:
#         print("NO")
        
# t = int(input())
# for _ in range(t):
#     n = input()
#     print(min(n))

# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     curr_summ = sum(arr[:k])
#     l = 0
#     i = k
#     res = 0
#     while i < n:
#         if curr_summ >= 1:
#             if i < n:
#                 curr_summ += arr[i]
#             curr_summ -= arr[l]
#             l += 1
#             i += 1
#         elif curr_summ == 0:
#             l += k
#             i += k
#             if i <= n:
#                 curr_summ = sum(arr[l:i])
#             res += 1
#     print(res)



# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     pref = [0] * (n + 1)
#     for i in range(n):
#         pref[i+1] = pref[i] + a[i]
#
#     res = 0
#     i = 0
#     while i <= n - k:
#         if pref[i+k] - pref[i] == 0:
#             res += 1
#             i += k + 1
#         else:
#             i += 1
#     print(res)


# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     if a == b:
#         print(0)
#     elif a % b == 0 or b % a == 0:
#         print(1)
#     else:
#         print(2)

# for _ in range(int(input())):
#     n,m = map(int, input().split())
#     a = list(map(int, input().split()))
#     lc = [0] * n
#     res = 0
#     for s in range(1, m + 1):
#         mc = 0
#         c = 0
        
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     a.sort(reverse=True)
#     k = min(n, m)
#     ans = 0
#     for i in range(k):
#         ans += a[i] * (m - i)
#     print(ans)


# t = int(input())
# for _ in range(t):
#     k ,x = map(int, input().split())
#     s = 1 << (k + 1)
#     a ,b = x , s - x
#     target = 1 << k
#     if a == target:
#         print(0)
#         continue
    
#     res = []
#     while a != target:
#         if a < b:
#             res.append(1)
#             b -= a
#             a <<= 1
#         else:
#             res.append(2)
#             a -= b
#             b <<= 1
#     res.reverse()
#     print(len(res))
#     if res:
#         print(*res)

# t = int(input())
# for _ in range(t):
#     x, n = map(int, input().split())
#     if n % 2 == 0:
#         print(0)
#     else:
#         print(x)

# ints = lambda: list(map(int, input().split()))
# t = int(input())
# for _ in range(t):
#     n, m, x, y = ints()
#     h = ints()
#     v = ints()
    
#     print(n + m)
   
# ints = lambda: map(int, input().split())
# t = int(input())
# for _ in range(t):
#     n, m = ints()
#     req = [tuple(ints()) for _ in range(n)]
#     res = 0
#     prevt, prevs = 0, 0
#     for a, b in req:
#         temp = a - prevt
#         if (temp % 2) == (prevs + b) % 2: 
#             res += temp
#         else:
#             res += temp - 1
#         prevt, prevs = a, b
#     res += m - prevt
#     print(res)
    
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     nechet = []
#     chet = 0
    
#     for i in range(n):
#         if a[i] % 2 == 0:
#             chet += a[i]
#         else:
#             nechet.append(a[i])
    
#     if len(nechet) == 0:
#         print(0)
#         continue
#     nechet.sort()
#     rest = 0
#     for i in range(len(nechet) // 2, len(nechet)):
#         rest += nechet[i]
#     print(rest + chet)


# ints = lambda: map(int, input().split())

# t = int(input())
# for _ in range(t):
#     n, k = ints()
#     a = list(ints())
    
#     all = [0] * (n + 1)
    
#     for i in range(n):
#         all[a[i]] += 1
    
#     cap = [0] * (n + 1)
#     flag = True
#     for i in range(1, n + 1):
#         if all[i] % k != 0:
#             flag = False
#             break
#         cap[i] = all[i] // k
        
#     if not flag:
#         print(0)
#         continue
    
#     cnt = [0] * (n + 1)
#     l = 0
#     res = 0
    
#     for r in range(n):
#         cnt[a[r]] += 1
#         while cnt[a[r]] > cap[a[r]]:
#             y = a[l]
#             cnt[y] -= 1
#             l += 1
#         res += r - l + 1
    
#     print(res)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     matrix = []
#     mx = 0
#     for _ in range(n):
#         rows = list(map(int, input().split()))
#         k = rows[0]
#         row = rows[1:]
#         matrix.append(row)
#         mx = max(mx, k)
    
#     matrix.sort()
    
#     res = [None] * mx
#     p = 0
#     for row in matrix:
#         while p < mx and p < len(row) and res[p] is None:
#             res[p] = row[p]
#             p += 1
#         if p == mx:
#             break
        
#     print(*res)