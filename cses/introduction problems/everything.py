# n = int(input())
# res = [n]
# while n != 1:
#     if n % 2 == 0:
#         n //= 2
#     else:
#         n  = (n * 3) + 1
#     res.append(n)
# print(*res)

# n= int(input())
# a = list(map(int, input().split()))
# s = (n * (n + 1)) // 2 - sum(i for i in a)
# print(s)

# s = input()
# prev = s[0]
# mx = 1
# cnt = 1
# for i in range(1, len(s)):
#     if s[i] == prev:
#         cnt += 1
#     else:
#         cnt = 1
#         prev = s[i]
#     mx = max(mx, cnt)
    
# print(mx)


# n = int(input())
# a = list(map(int, input().split()))
# s = 0
# for i in range(1, n):
#     if a[i] < a[i-1]:
#         s += a[i-1] - a[i]
#         a[i] = a[i-1]
# print(s)


# n = int(input())
# p = [0] * (n)
# if n >= 4 or n == 1:
#     elem = 2
#     for i in range(n//2):
#         p[i] = elem
#         elem+=2
        
#     elem = 1
#     for i in range(n//2, n):
#         p[i] = elem
#         elem += 2
#     print(*p)
# else:
#     print("NO SOLUTION")

# t = int(input())
# for _ in range(t):
#     x, y = map(int, input().split())
#     if x == y:
#         print((x * y) - (y - 1))
#     elif x > y:
#         d = (x * x) - (x - 1)
#         if x % 2 != 0:
#             print(d - (x - y))
#         else:
#             print(d + (x - y))
#     else:
#         d = (y * y) - (y - 1)
#         if y % 2 != 0:
#             print(d - (x - y))
#         else:
#             print(d + (x - y))
            
# n = int(input())
# for i in range(1, n+1):
#     f = ((i ** 2) * ((i ** 2) - 1)) // 2
#     fs = 4 * ((i - 1) * (i - 2))
#     print(f - fs)

# not done yet
# n = int(input())
# if (n * ( n + 1)) // 2 != 0:
#     print("NO")
# else:
#     print("YES")

# if n % 2 == 0:
    
    
# n = int(input())
# print((2 ** n) % (10 **9 + 7))


# not done yet
# t = int(input())
# for _ in range(t):
#     a ,b = map(int, input().split())
#     if 
        
# n = int(input())
# cnt = 0
# i = 5
# while n // i >= 1:
#     cnt += (n // i)
#     i *= 5
# print(cnt)

# s = input()
# mp = {}
# for i in s:
#     if i not in mp:
#         mp[i] = 1
#     else:
#         mp[i] += 1
# chet = nechet = 0
# for key, value in mp.items():
#     if value % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1

# start = ""
# mid = ""
# end = ""
# if nechet < 2 and chet >= 0:
#     for key, value in mp.items():
#         if mp[key] % 2 == 0:
#             start += (key * (mp[key] // 2))
#         else:
#             mid += (key * mp[key])
# else:
#     print("NO SOLUTION")
# end = start[::-1]
# res = start + mid + end
# print(res)

# def bin(n: int):
#     res = ""
#     if n == 0:
#         for i in range(n):
#             res += "0"
#         return res
    
#     res = ""
#     while n > 1:
#         if n % 2 == 0:
#             res += "0"
#         else:
#             res += "1"
#         n //= 2
#     res = str(n) + res[::-1]
#     return res 

# n = int(input())
# for temp in range((1 << n)):
#     i = temp
#     res = ["0"] * n
#     if i == 0:
#         print("".join(res))
#         continue
#     idx = n - 1
#     while i > 1:
#         if i % 2 != 0:
#             res[idx] = str(1)
#         i //= 2
#         idx -= 1
#     res[idx] = str(i)
#     print("".join(res)) 


