
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
        
#         l += 1
#         r -= 1
#     print(n - x)
    

