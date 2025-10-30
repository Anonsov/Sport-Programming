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


# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     ps = []
#     t = 0
#     for i in range(n):
#         t += a[i]
#         ps.append(t)
        
#     flag = False
#     for l in range(1, n -1):
#         for r in range(l + 1, n):
#             s1 = ps[l-1] % 3
#             s2 = (ps[r-1] - ps[l-1]) % 3
#             s3 = (ps[n-1] - ps[r-1]) % 3
#             if (s1 == s2 == s3) or (s1 != s2 and s2 != s3 and s1 != s3):
#                 print(l, r)
#                 flag = True
#                 break
#         if flag:
#             break  
#     if not flag:
#         print(0, 0)


# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     est = set(x for x in a if x != 0)
#     miss = []
#     for i in range(1, n + 1):
#         if i not in est:
#             miss.append(i)
#     zeros = [i for i in range(n) if a[i] == 0]
#     mxc = 0
#     t = a.copy()
#     for i, pos in enumerate(zeros):
#         t[pos] = miss[i]
#     l, r = -1, -1
#     for i in range(n):
#         if t[i] != i + 1:
#             if l == -1:
#                 l = i
#             r = i
#     c = 0 if l == -1 else r - l + 1
#     mxc = max(mxc, c)
#     print(mxc)
    
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     p = [0] * (n + 1)
#     for i in range(n):
#         p[a[i]] = i

#     l = r = p[n]
#     flag = True
#     for x in range(n - 1, 0, -1):
#         if p[x] < l:
#             l = p[x]
#         if p[x] > r:
#             r = p[x]
#         if r - l + 1 != n - x + 1:
#             flag = False
#             break
    
#     if flag:
#         print("YES")
#     else:
#         print("NO") 



# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     a.sort()
#     b.sort()
#     l = 0
#     r = n - 1
#     s = 0
#     pref = [0] * (n + 1)
#     for i in range(n):
#         pref[i + 1] = pref[i] + a[i]
#     for i in range(k):
#         f = r - (b[i] - 1)
#         if f < l:
#             continue
#         if f + 1 <= r:
#             s += pref[r + 1] - pref[f + 1]
#         r = f - 1
#         if r < l:
#             break
#     if r >= l:
#         s += pref[r + 1] - pref[l]
    
#     print(s)
# from sys import setrecursionlimit
# setrecursionlimit(200000)
# for _ in range(int(input())):
#     n = int(input())
#     g = [[]for _ in range(n + 1)]
#     for i in range(n - 1):
#         u, v, x, y = map(int, input().split())
#         if x >= y:
#             g[v].append(u)
#         else:
#             g[u].append(v)
 
#     used = [False] * (n + 1)
#     o = []
    
#     def dfs(v):
#         used[v] = True
#         for i in g[v]:
#             if not used[i]:
#                 dfs(i)
#         o.append(v)
    
#     for i in range(1, n + 1):
#         if not used[i]:
#             dfs(i)
    
#     t = o[::-1]
#     p = [0] * (n + 1)
#     idx = 1
#     for i in t:
#         p[i] = idx
#         idx += 1       
    
#     print(*p[1:])



# t = int(input())
# for _ in range(t):
#     x, y = map(int, input().split())
#     if y == 1:
#         print(-1)
#     elif x < y:
#         print(2)
#     elif x >= y + 2:
#         print(3)
#     else:
#         print(-1)

# t = int(input())
# for _ in range(t):
#     n = int(input())

#     dp = [0] * ((2*n) + 1)
#     used = [False] * ((2*n) + 1)
#     l = 1
#     for i in range(n, 0, -1):
#         while used[l]:
#             l += 1
#         j = l + i
#         while j <= 2 * n and used[j]:
#             j += i
#         dp[l] = i
#         dp[j] = i
#         used[l] = True
#         used[j] = True
#     print(*dp[1:])
            
            
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
#     i = 0
#     flag = True
#     while i < n:
#         if s[i] == '0':
#             if i + 1 < n and s[i+1] == '0':
#                 while i < n and s[i] == '0':
#                     i += 1
#                 continue
#             j = i
#             cnt = 1
#             while j + 2 < n and s[j + 1] == '1' and s[j + 2] == '0':
#                 j += 2
#                 cnt += 1
#             if cnt % 2 == 1 and i != 0 and j != n - 1:
#                 flag = False
#                 break
#             i = j + 1
#         else:
#             i += 1
#     if flag:
#         print("YES")
#     else:
#         print("NO")
        
        
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
    
#     if '0' not in s:
#         print("YES")
#         continue
#     z = []
#     for i in range(n):
#         if s[i] == '0':
#             z.append(i)
#     i = 0
#     flag = True
#     while i < len(z):
#         if i + 1 < len(z) and z[i+1] == z[i] + 1:
#             while i + 1< len(z) and z[i + 1] == z[i] + 1:
#                 i += 1
#             i += 1
#             continue
#         j = i
#         while j + 1 < len(z) and z[j + 1] == z[j] + 2:
#             j += 1
        
#         if (j - i + 1) % 2 == 1 and z[i] != 0 and z[j] != n - 1:
#             flag = False
#             break
#         i = j + 1
    
#     if flag:
#         print("YES")
#     else:
#         print("NO")
            
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     mp = {}
#     s = 0
#     for i in a:
#         s += i
#         if i in mp:
#             mp[i] += 1
#         else:
#             mp[i] = 1
#     alice = 0
#     bob = 0
#     t = 0
#     for i in sorted(mp.keys()):
#         cnt = mp[i]
#         if t == 0:
#             alice += cnt * ((i + 1) // 2)
#         else:
#             alice += cnt * (i // 2)
#         if i % 2 == 1:
#             t = 1 - t
#     bob = s - alice
#     print(alice, bob)
    
    
# for i in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     dp = [0] * (n + 1)
#     for i in range(n):
#         dp[a[i]] += 1
        
#     mx = 0
#     for i in range(1, max(dp) + 1):
#         s = 0
#         for j in range(1, n + 1):
#             if dp[j] >= i:
#                 s += 1
#         mx = max(mx, i * s)    
#     print(mx)


# for _ in range(int(input())):
#     n, m = map(int,input().split())
#     dp = []
#     for i in range(n):
#         a = list(map(int, input().split()))
#         s = set(a[1:])
#         dp.append(s)
        
#     all = set()
#     for i in dp:
#         all.update(i)
    
#     if len(all) < m:
#         print("NO")
#         continue
    
#     r = set()
#     for i in range(1, m + 1):
#         found = []
#         for j in range(n):
#             if i in dp[j]:
#                 found.append(j)
#         if len(found) == 1:
#             r.add(found[0])
    
#     cnt = 0
#     for i in range(1, 1 << n):
#         flag = True
#         for j in r:
#             if (i & (1<<j)) == 0:
#                 flag = False
#                 break
    
#         if not flag:
#             continue
#         cover = [False] * (m + 1)

#         for j in range(n):
#             if (i & (1 << j)) != 0:
#                 for k in dp[j]:
#                     cover[k] = True
        
#         flag = True
#         for i in range(1, m + 1):
#             if not cover[i]:
#                 flag = False
#                 break
        
#         if flag:
#             cnt += 1
#             if cnt >= 3:
#                 print("YES")
#                 break
#     else:
#         print("NO")
        
        
# for _ in range(int(input())):
#     n, m = map(int,input().split())
#     dp = []
#     cnt = [0] * (m + 1)

#     for i in range(n):
#         a = list(map(int, input().split()))
#         s = set(a[1:])
#         dp.append(s)
#         for j in s:
#             cnt[j] += 1
    
#     flag = True
#     for i in range(1, m+ 1):
#         if cnt[i] == 0:
#             flag = False
#             break
#     if not flag:
#         print("NO")
#         continue
    
#     disc = 0
#     for i in range(n):
#         flag = True
#         for j in dp[i]:
#             if cnt[j] < 2:
#                 flag = False
#                 break
#         if flag:
#             disc += 1
    
#     if disc >= 2:
#         print("YES")
#     else:
#         print("NO")

# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     ones = 0
#     for i in s:
#         if i == '1':
#             ones += 1
#     if ones == 0:
#         dp = [0] * n
#         for i in range(n - 1):
#             dp[i] = i + 2
#         dp[n-1] = 1
#         print('YES')
#         print(*dp)
#         continue
    
#     dp = [0] * (n + 1)
#     flag = True
#     i = 1
#     while i <= n:
#         if s[i-1] == '1':
#             dp[i] = i
#             i += 1
#         else:
#             l = i
#             while i <= n and s[i - 1] == '0':
#                 i += 1
#             r = i - 1
#             if r - l + 1 == 1:
#                 flag = False
#                 break
#             for j in range(l, r):
#                 dp[j] = j + 1
#             dp[r] = l
    
#     if not flag:
#         print("NO")
#     else:
#         print("YES")
#         print(*dp[1:])

