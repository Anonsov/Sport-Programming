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



# import collections

