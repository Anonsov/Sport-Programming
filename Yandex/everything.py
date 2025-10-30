# n = int(input())
# song_count = {}
# for i in range(n):
#     k = int(input())
#     songs = input().split()
#     for song in songs:
#         if song in song_count:
#             song_count[song] += 1
#         else:
#             song_count[song] = 1
# result = []
# for song, count in song_count.items():
#     if count == n:
#         result.append(song)
# result.sort()

# print(len(result))
# if len(result) > 0:
#     print(' '.join(result))


# res = {}
# res2 = {}
# def solve(a: str , b: str) -> bool:
#     if len(a) != len(b):
#         return False
    
#     for i in range(len(a)):
#         if a[i] in res:
#             res[a[i]] += 1
#         else:
#             res[a[i]] = 1
        
#         if b[i] in res2:
#             res2[b[i]] += 1
#         else:
#             res2[b[i]] = 1
    
#     return res == res2
    
# a = input()
# b = input()
# bl = solve(a, b)
# if bl:
# 	print("YES")
# else:
#     print("NO")


# n = int(input())
# a = list(map(int, input().split()))
# s = set()
# res = {}
# mn = float('inf')

# for i in range(n):
#     if a[i] in res:
#         res[a[i]] += 1
#     else:
#         res[a[i]] = 1
    
#     s.add(a[i])
# s = sorted(s)

# mx = 0

# found = False
# for i in range(1, len(s)):
#     if s[i] - s[i - 1] <= 1:
#         mn = min(mn, n - (res[s[i - 1]] + res[s[i]]))
#         found = True

        
# if found:
#     if mn == float('inf'):
#         print(0)
#     else:
#         print(mn)
# else:
#     print(n - mx)



# def isPalindrome( s: str) -> bool:
#     flag = True
#     n = len(s)
#     l = 0
#     r = n - 1
#     while l < r:
#         while s[l] == " " or not 97 <= ord(s[l].lower()) <= 122:
#             l += 1
#         while s[r] == " " or not 97 <= ord(s[r].lower()) <= 122:
#             r -= 1
        
#         if s[l].lower() != s[r].lower():
#             flag = False
#             print(s[l].lower(), s[r].lower())
#             break
#         print(s[l].lower(), l, s[r].lower(), r)
#         l += 1
#         r -= 1
#     return flag

# print(isPalindrome("A man, a plan, a canal: Panama"))
# print(isPalindrome("race a car"))

# a, b, c = map(int, input().split())
# n = int(input())

# from math import gcd
# def nok(a, b):
#     return a // gcd(a, b) * b

# nok_ab = nok(a, b)
# nok_ac = nok(a, c)
# nok_bc = nok(b, c) 
# nok_abc = nok(nok_ab, c) 


# def checker(x):
#     cnt_ab = x // nok_ab - x // nok_abc  
#     cnt_ac = x // nok_ac - x // nok_abc  
#     cnt_bc = x // nok_bc - x // nok_abc  
#     return cnt_ab + cnt_ac + cnt_bc

# l = 1
# r = 10**18
# res = -1

# while l < r:
#     m = (l + r) // 2
#     if checker(m) >= n:
#         res = m
#         r = m - 1
#     else:
#         l = m + 1
        
# print(res)


# a, b, c = map(int, input().split())
# n = int(input())

# mx = 10**18
# from math import gcd
# def nok(a, b):

#     g = gcd(a,b)
#     t = a // g
#     if t > mx // b:
#         return mx + 1
#     return t * b




# def checker(x, a, b, c, nok_ab, nok_bc, nok_ac, nok_abc):
#     cnt_ab = x // nok_ab - x // nok_abc  
#     cnt_ac = x // nok_ac - x // nok_abc  
#     cnt_bc = x // nok_bc - x // nok_abc  
#     return cnt_ab + cnt_ac + cnt_bc


# def solve(a,b,c,n):
#     nok_ab = nok(a, b)
#     nok_ac = nok(a, c)
#     nok_bc = nok(b, c) 
#     nok_abc = nok(nok_ab, c) 
#     if nok_ab > mx:
#         nok_abc = mx + 1
#     else:
#         nok_abc = nok(nok_ab, c)
    
#     if checker(mx, a,b,c, nok_ab, nok_ac, nok_bc, nok_abc) < n:
#         return -1
#     l = 1
#     r = mx
#     res = -1

#     while l <= r:
#         m = (l + r) // 2
#         if checker(m) >= n:
#             res = m
#             r = m - 1
#         else:
#             l = m + 1


        
# print(res)