
# n = int(input())
# arr = list(map(int, input().split()))
# q = int(input())
# for i in range(0, q):
#     c = list(map(int, input().split()))
#     for i in range(0, len(arr)):
#         if c[0] <= i <= c[1]:
#             arr[i - 1] += c[-1]

# print(arr)     

# n = 4
# a1 = 1
# a2 = 1
# for i in range(0, n-1):
#     a1, a2 = a2, a1+a2
# print(a1)


# a = list(map(int, input().split()))
# res = {}
# for i in a:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1

# for i in res:
#     if res[i] == 2:
#         print(i)

# k = int(input())



# st = list(map(str, input().split(".")))
# flag = True
# print(st)
# for i in st:
#     for j in i:
#         if (ord(j) == 0 or 49 <= ord(j) <= 57) and (len(st) == 4):
#             flag = True
#         else:
#             flag = False
#             break
# if flag:
#     print("YES")
# else:
#     print("NO")


# st = input().split(".")
# flag = True
# if len(st) == 4:
#     for i in st:
#         if i.isdigit():
#             s = int(i)
#             if (0 <= s <= 255) == False:
#                 flag = False
#                 break
#         else:
#             flag = False
# else:
#     flag = False

# if flag:
#     print("YES")
# else:
#     print("NO")
    
    
# print("0F4".isdigit())

# import math
# n = int(input())
# c = 0
# for i in range(1, int(math.sqrt(n)) + 1):
#     if n%i == 0:
#         c+=2
#         if i*i == n:
#             c-=1
# print(c)
            
            
# a,b,c = map(int, input().split())
# s1 = a//c
# s2 = b//c
# res = s1*s2
# print(res)            

# map_counter = {}
# s = 0
# res = []

# st = input()

# for i in st:
#     if i in map_counter:
#         map_counter[i] +=1
#     else:
#         map_counter[i] = 1
    
#     if map_counter[i] % 2 == 0:
#         s-=1
#     else:
#         s+=1
    
#     if s <= 1:
#         res.append("YES")
#     else:
#         res.append("NO")
        
# print(*res)



# from math import sqrt
# n = int(input())
# res = {}
# res = []
# for i in range(2, int(sqrt(n))+2):
#     res.append()
         



# В магазине есть N (1 ≤ N ≤ 100) мячиков и K (1 ≤ K ≤ 100) видов краски. Мячики лежат в одном ряду. Продавец хочет покрасить все мячики, но при этом условие не должно нарушатся. Условие в том, что никакие 2 соседние мячики не должны иметь одинаковый цвет. Вы должны найти, сколькими вариантами можно это сделать. Если ответ слишком большой, нужно вывести его с остатком от 1000000007.

# n, s = map(int, input().split())
# res = s // n
# if s % n != 0:
#     res += 1
# print(res)


# t = int(input())
# l = list(map(int, input().split()))
# res = {}
# a = 0
# for i in l:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1
    
#     if res[i] == 4:
#         a = i

# if a == 0:
#     print(-1)
# else:
#     print(a)

# n = int(input())
# if n % 3 == 2:
#     d = n//3
#     s = ""
#     for i in range(n):
#         if (i + 1) % 3==0:
#             row = ""
#             for j in range(1, n+1):
#                 if (j+1) % 3 == 0:
#                     row += "+"
#                 else:
#                     row += "-"
#             print(row)
#         else:
#             row = ""
#             for j in range(1, n+1):
#                 if (j+1) % 3 == 0:
#                     row += "|"
#                 else:
#                     row += "."
#             print(row)
            
# else:
#     print(".-+|")         
# matrix = []
# n, m = map(int, input().split())
# maxim = float('-inf')
# for i in range(n):
#     row = list(map(int, input().split()))
#     curr = max(row)
#     if maxim < curr:
#         maxim = curr
#     matrix.append(row)

# l = len(str(maxim)) + 1

# for i in matrix:
#     s = ""
#     for j in i:
#         cnt = len(str(j))
#         s += ((l - cnt) * "_") + str(j)
#     print(s)

# n = int(input())
# a = list(map(int, input().split()))
# k = int(input())
# res = set()
# found = False
# for i in a:
#     if k % i == 0:
#         s = k // i
#         if s in res:
#             print(i, s)
#             found = True
#             break
#         res.add(i)

# if not found:
#     print(-1)
    
    
# n, s = list(input().split())
# arr = set(map(str, input().split()))
# if s in arr:
#     print("YES")
# else:
#     print("NO")


# n, m = list(map(int, input().split()))
# matrix = []
# nmatrix = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# for i in range(m):
#     row = []
#     for j in range(n - 1, -1, -1):
#         row.append(matrix[j][i])
#     nmatrix.append(row)

# for row in nmatrix:
#     print(*row)

# s = input()
# a = ['(', '{', '[']
# b = [')', '}', ']']
# x = []

# for i in s:
#     if i in a:
#         x.append(i)
#     elif i in b:
#         if not x or b.index(i) != a.index(x.pop()):
#             print("NO")
#             break
# if not x:
#     print("YES")

# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(0, n - 1, 2):
#     arr[i], arr[i + 1] = arr[i + 1], arr[i]

# print(*arr)

# t = int(input())
# l = list(map(int, input().split()))
# res = set()
# j = 0
# for i in l:
#     res.add(i)    
# print(len(res))


# n = int(input())
# arr = list(map(int, input().split()))
# res = {}
# a = 0

# for num in arr:
#     if num in res:
#         res[num] += 1
#     else:
#         res[num] = 1

# for cnt in res.values():
#     if cnt > 1:
#         a += 1

# print(a)

# n = int(input())
# words = input().split()
# res = {}
# min_lex = 0
# for i in words:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1

#         max_cnt = 0
#         for cnt in res.values():
#             if cnt > max_cnt:
#                 max_cnt = cnt

#         cnter = []
#         for i, cnt in res.items():
#             if cnt == max_cnt:
#                 cnter.append(i)

#         min_lex = cnter[0]
#         for i in cnter:
#             if i < min_lex:
#                 min_lex = i

# print(min_lex)

# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0
# res = {}

# for i in arr:
#     if i + k in res:
#         cnt += res[i + k]
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1

# print(cnt)
# from random import randint
# m = 6
# n = 5
# matrix = []
# for i in range(m):
#     row = []
#     for j in range(m):
#         row.append(0)
#     matrix.append(row)
    
# for i in matrix:
#     print(*i)   
  
  
# print()
# print()
# print()
  
  
  
  
  
# m = 6
# x = 1
# for d in range(2 * m - 1):
#     if d < m:
#         if d % 2 == 0:
#             i = d
#             j = 0
#             while i >= 0 and j < m:
#                 matrix[i][j] = x
#                 x += 1
#                 i -= 1
#                 j += 1
#         else:
#             i = 0
#             j = d
#             while i < m and j >= 0:
#                 matrix[i][j] = x 
#                 x += 1
#                 i += 1
#                 j -= 1
#     else:
#         if d % 2 == 0:
#             i = m - 1
#             j = d - (m - 1)
#             while i > 0 and j < m:
#                 matrix[i][j] = x
#                 j += 1
#                 i -= 1
#                 x += 1
#         else:
#             i = d - m - 1
#             j = m - 1
#             while i < m and j > 0:
#                 matrix[i][j] = x
#                 i += 1
#                 j -= 1
#                 x += 1


        
# for i in matrix:
#     print(*i)
        
        
# n, q = map(int, input().split())
# currs = sorted(list(map(int, input().split())))
# targets = list(map(int, input().split()))

# for target in targets:
#     l = 0
#     r = n - 1
#     result = -1
#     while l <= r:
#         mid = (l + r) // 2
#         if currs[mid] >= target:
#             result = currs[mid]
#             r = mid - 1
#         else:
#             l = mid + 1
#     print(result)


# from math import sqrt
# c = int(input())
# l = 0
# r = c
# while r - l > 1:
#     mid = (l+r) / 2
#     res = sqrt(mid) + mid ** 2
#     if res < c:
#         l = mid
#     else:
#         r = mid

# print(r, l)
    
# for target in targets:
#     curr = currs
#     found = False
#     while len(curr) > 1:
#         center = (len(curr)) // 2
#         left = curr[:center]
#         right = curr[center:]
#         if target <= left[-1]:
#             curr = left
#         elif target >= right[0]:
#             curr = right
#         else:
#             break
#     if curr and curr[0] == target:
#         found = True

#     if found:
#         print("YES")
#     else:
#         print("NO")

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
#     l = 0
#     r = n - 1
#     x = 0
#     while l<=r:
#         if s[l] != s[r]:
#             x += 2
#         elif s[l] == s[r]:
#             break
#
#         l += 1
#         r -= 1
#     print(n - x)
    


# def uyobishnaya_recursiya(n, curr=""):
#     if len(curr) == n:
#         print(curr)
#         return
#     uyobishnaya_recursiya(n, curr + "0")
#     if not curr or curr[-1] != "1":
#         uyobishnaya_recursiya(n, curr + "1")

# uyobishnaya_recursiya(int(input()))


# n = int(input())
# a = list(map(int, input().split()))
# for i in range(0, n - 1, 2):
#     a[i], a[i + 1] = a[i + 1], a[i]
# print(*a)


# st = input().split(".")
# flag = True
# if len(st) == 4:
#     for i in st:
#         if i.isdigit():
#             s = int(i)
#             if (0 <= s <= 255) == False:
#                 flag = False
#                 break
#         else:
#             flag = False
# else:
#     flag = False

# if flag:
#     print("YES")
# else:
#     print("NO")





# a, s = input().split()
# s = int(s)
# h, m, sec = map(int, a.split(':'))
# ts = h * 3600 + m * 60 + sec
# ts -= s
# while ts < 0:
#     ts += 86400
# nh = ts // 3600
# nm = (ts % 3600) // 60
# ns = ts % 60
# print(f"{nh:02}:{nm:02}:{ns:02}")






# n = int(input())
# a = list(map(int, input().split()))
# k = int(input())

# res = set()
# found = False
# for i in a:
#     if k % i == 0:
#         s = k // i
#         if s in res:
#             print(i, s)
#             found = True
#             break
#         res.add(i)

# if not found:
#     print(-1)




# a = list(map(int, input().split()))
# res = {}
# un = set()
# for i in range(len(a)):
#     if a[i] in res:
#         res[a[i]] += 1
#     else:
#         res[a[i]] = 1
#     un.add(a[i])

# for i in un:
#     if res[i] == 2:
#         print(i)
#         break


# s = input()
# def num(expr):
#     expr_num = ""
#     if "*" in expr or "+" in expr:
#         for i in range(len(expr)):
#             if expr[i] == "*" or expr[i] == "+":
#                 break
#             expr_num += expr[i]
#     else:
#         expr_num = expr
#     return int(expr_num)


# def calc(curr_s: str):
#     result = num(curr_s)
#     i = 0
#     while i < len(curr_s) and curr_s[i].isdigit():
#         i += 1
#     while i < len(curr_s):
#         if curr_s[i] == "+":
#             result += num(curr_s[i+1:])
#         elif curr_s[i] == "*":
#             result *= num(curr_s[i+1:])
#         i += 1
#         while i < len(curr_s) and curr_s[i].isdigit():
#             i += 1
#     return result

# def fb(expr):
#     s = -1
#     for i in range(len(expr)):
#         if expr[i] == '(':
#             s = i
#         elif expr[i] == ')':
#             return s, i
#     return -1, -1

# def se(expr):
#     while '(' in expr:
#         i, j  = fb(expr)
#         if i == -1:
#             break
#         nexpr = expr[i+1:j]
#         result = calc(nexpr)
#         expr = expr[:i] + str(result) + expr[j+1:]
#     return calc(expr)

# print(se(s))
# n = int(input())
# k = 0
# x = 2
# while x * x <= n:
#     while n % x == 0:
#         k += 1
#         n //= x
#     x += 1
# if n > 1:
#     k += 1
# print(k)

# wx1, wy1, wx2, wy2 = map(int, input().split())
# bx1_1, by1_1, bx2_1, by2_1 = map(int, input().split()) 
# bx1_2, by1_2, bx2_2, by2_2 = map(int, input().split())

# l = min(bx1_1, bx1_2)
# r = max(bx2_1, bx2_2)
# t = max(by1_1, by1_2)
# b = min(by2_1, by2_2)


# if l <= wx1 and r >= wx2 and t >= wy1 and b <= wy2:
#     print("YES")
# else:
#     print("NO")


# n = int(input())
# a = list(map(int, input().split()))
# cnt = 1
# mx = cnt
# for i in range(1, n):
#     if a[i] == a[i - 1]:
#         cnt += 1
#     else:
#         cnt = 1
#     if cnt > mx:
#         mx = cnt
# print(mx)



# На шахтном участке расположены n шахт на линии. Нужно построить ровно k станций снабжения. Каждая шахта должна быть прикреплена к ближайшей станции. Найти минимально возможное значение максимального расстояния от шахты до станции.

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort()
# res = []





# Камера снимает каждый кадр с энергозатратой. Нужно выбрать непрерывный отрезок кадров, суммарная энергия которого ≤ k, при этом отрезок максимальной длины.

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# l = 0
# r = 0
# s = 0
# max_len = 0
# while r < n:
#     s += a[r]
#     while s > k:
#         s -= a[l]
#         l += 1
#     max_len = max(max_len, r - l + 1)
#     r += 1
# print(max_len)



# graphs
# n, m = map(int, input().split())
# for i in range(m):
#     u, v = map(int, input().split())
# if n - m == 1:
#     print("YES")
# else:
#     print("NO")


# n, m = map(int, input().split())
# for i in range(m):
#     u, v = map(int, input().split())
# if n - m > 1:
#     print("YES")
# else:
#     print("NO")


# FIRST                        

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


# second 
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


# THIRD
# n, m = map(int, input().split())
# g = [[] for ii in range(n + 1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     g[v].append(u)
#     g[u].append(v)


# used = [False for i in range(n + 1)]
# def dfs(v):
#     if used[v]:
#         return
#     used[v] = True
#     for i in g[v]:
#         dfs(i)
# s = 0

# for i in range(1, n + 1):
#     if not used[i]:
#         s += 1
#         dfs(i)
        
# print(s)


# ints = lambda: map(int, input().split())
# n, m = ints()
# a, b = ints()

# g: list[list[int | None]] = [[] for i in range(n + 1)]

# for i in range(m):
#     u, v = ints()
#     g[v].append(u)
#     g[u].append(v)

# used: list[bool] = [False for i in range(n + 1)]

# def dfs(v: int) -> None:
#     if used[v]:
#         return
#     used[v] = True
    
#     for i in g[v]:
#         dfs(i)

# dfs(a)


# if used[b]:
#     print("YES")
# else:
#     print("NO")









        

    

# def solve(n, m):
#     if m > n:
#         print(-1)
#         return
    
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append(0)
#         matrix.append(row)
    
        
#     edges = 0
#     smezhnosti = []
    
#     for i in range(1, n - m + 1):
#         for j in range(i):
#             matrix[i][j] = 1
#             matrix[j][i] = 1
#             edges += 1
#             smezhnosti.append([i + 1, j+ 1])
            
#     print(edges)
#     for i in smezhnosti:
#         print(*i)
        
# n, m = map(int, input().split())
# solve(n, m)



# def solve(n, m):
#     if m < 1 or m > n:
#         print(-1)
#         return
    
#     if n - m > 10**5:
#         print(-1)
#         return 

#     if m == n:
#         print(0)
#         return
    
#     res = []
#     for i in range(1, n - m + 1):
#         res.append([i, i+1])
    
#     print(len(res))
#     for i in res:
#         print(*i)
        
# n, m = map(int, input().split())
# solve(n, m)


# import sys
# sys.setrecursionlimit(10**5 + 7)

# n, m = map(int, input().split())
# g = [[]for i in range(n + 1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)

# stepeni = 0
# used = [False for i in range(n + 1)]
# def dfs(v: int):
#     global stepeni
#     if used[v]:
#         return 0
#     used[v] = True
    
#     stepeni += len(g[v])
#     cnt = 1
#     for i in g[v]:
#         cnt += dfs(i)
    
#     return cnt
    
    
# res= 0
# for i in range(1, n + 1):
#     if not used[i]:
#         stepeni = 0
#         vershini = dfs(i)
#         es = stepeni // 2
#         res += es - (vershini - 1)
        
# print(res)




# Новая попытка Б задачи
# import sys
# sys.setrecursionlimit(10**5 + 7)
# vertices = 0
# edges = 0

# n, m = map(int, input().split())
# g = [[]for i in range(n + 1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)
    
    
# used  = [False for i in range(n + 1)]


# def dfs(v: int):
#     global vertices, edges
    
#     if used[v]:
#         return
#     used[v] = True
#     edges += len(g[v])
#     vertices += 1
#     for i in g[v]:
#         dfs(i)
# res = 0
# for i in range(1, n + 1):
#     if not used[i]:
#         vertices = 0
#         edges = 0
#         dfs(i)
#         res += (edges // 2) - (vertices - 1)
# print(res)



# n, m = map(int, input().split())
# g = [[]for i in range(n + 1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)
    
# used = [False for i in range(n + 1)]    

# p = [0] * (n + 1)
# d = [0] * (n + 1)
# def dfs(v: int):
#     global p, d
#     if used[v]:
        
#         return
#     used[v] = True
    
#     for i in g[v]:
#         dfs(i)
            
    
# for i in range(1, n + 1):
#     if not used[i]:
        
#         dfs(i)


# ОСТРОВА
# from sys import setrecursionlimit
# setrecursionlimit(10**5 + 7)
# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# cnt = 0
# def dfs(i, j):
#     global cnt
#     if i >= n or j >= m or i < 0 or j < 0 or matrix[i][j] == 0:
#         return
#     matrix[i][j] = 0
#     cnt += 1
#     dfs(i, j - 1)
#     dfs(i - 1, j)
#     dfs(i, j + 1)
#     dfs(i + 1, j)
    
    
    
# res = []
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] == 1:
#             cnt = 0
#             dfs(i, j)
#             res.append(cnt)
# res.sort()
# print(len(res))
# print(*res)


# Подсчет детей
# n, m = map(int, input().split())
# g = [[] for i in range(n + 1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     g[u].append(v)

# a = int(input())
# print(len(g[a]))



# from sys import setrecursionlimit
# setrecursionlimit(10**5 + 7)
# ints = lambda: map(int, input().split())

# n, m = ints()
# s = 0
# g = [[] for i in range(n + 1)]
# used = [False for i in range(n + 1)]

# for i in range(m):
#     u, v = ints()
#     g[u].append(v)
#     g[v].append(u)

# comps = [0] * (n + 1)
# def dfs(v: int):
#     global s
#     if used[v]:
#         return
#     used[v] = True
#     comps[v] = s
#     for i in g[v]:
#         dfs(i)
        
        
# for i in range(1, n + 1):
#     if not used[i]:
#         s += 1
#         dfs(i)
    
# q = int(input())

# for i in range(q):
#     u ,v = ints()
#     if comps[u] == comps[v]:
#         print("YES")
#     else:
#         print("NO")



# from sys import setrecursionlimit
# from collections import deque
# setrecursionlimit(10**5 + 7)
# ints = lambda: map(int, input().split())
# res = 0
# n, m = ints()
# g = [[] for i in range(n + 1)]
# used = [False for i in range(n + 1)]

# for i in range(m):
#     u, v = ints()
#     g[u].append(v)
    
# a = int(input())

# def dfs(v: int):
#     global res
#     if used[v]:
#         return
    
#     used[v]= True
#     res += 1
#     for i in g[v]:
#         dfs(i)

# vertices = deque()
# for i in g[a]:
#     vertices.append(i)

# while vertices:
#     v = vertices.popleft()
#     used[v] = True
#     res += 1
#     for i in g[v]:
#         if not used[i]:
#             vertices.append(i)
    
        
# print(res)



# ints = lambda: map(int, input().split())
# from sys import setrecursionlimit
# setrecursionlimit(10**5 + 7)

# n, k = ints()

# g = [[] for i in range(n + 1)]
# used = [False for i in range(n + 1)]
# res = [0] * (n + 1)

# for i in range(n - 1):
#     u, v = ints()
#     g[u].append(v)
#     g[v].append(u)
    
    
# def dfs(v: int, p = -1):
#     if used[v]:
#         return 0
    
#     used[v] = True
#     c = 1
#     for i in g[v]:
#         if i != p:
#             c += dfs(i, v)
#     res[v] = c        
#     return c

# dfs(k)

# print(*res[1:])


def m(fx, fy, sx, sy):
    return abs(fx - sx) + abs(fy - sy)

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
dist = m(ax, ay, bx, by)
print(dist)

cx, cy = bx, by + dist
cx1, cy1 = bx + dist, by

print(cx, cy, cx1, cy1)
formula = (m(ax, ay, cx, cy) == m(bx, by, cx, cy))
print(formula)

