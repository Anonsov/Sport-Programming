# n = int(input())
# a = list(map(int, input().split()))
# mp = {}

# for i in a:
#     if i not in mp:
#         mp[i] = 1
# print(len(mp))


# n, m, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a.sort()
# b.sort()
# i = 0
# j = 0
# cnt = 0
# while i < n and j < m:
#     if a[i] - k <= b[j] <= a[i] + k:
#         i += 1
#         j += 1
#         cnt += 1
#     elif a[i] + k < b[j]:
#         i += 1
#     elif a[i] - k > b[j]:
#         j += 1
# print(cnt)

# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort()
# l = 0
# r = n - 1
# res = 0
# while l <= r:
#     if a[l] + a[r] <= x:
#         l += 1
#         r -= 1
#     else:
#         r -= 1
#     res += 1

# print(res)



