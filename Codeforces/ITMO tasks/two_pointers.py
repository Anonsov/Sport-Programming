# # ИТМО КРУЖОК ДВА УКАЗАТЕЛЯ №1
# n, m = map(int, input().split())
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# res = []
# f = 0
# s = 0
# while f < n and s < m:
#     if arr1[f] <= arr2[s] :
#         res.append(arr1[f])
#         f += 1
#     elif arr2[s] <= arr1[f]:
#         res.append(arr2[s])
#         s += 1
# if f != n:
#     for i in arr1[f:]:
#         res.append(i)
#
# if s != m:
#     for i in arr2[s:]:
#         res.append(i)
# print(*res)

# ЗАДАЧА Б число меньших
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# res = []
# f = 0
# s = 0
#
# while s < m:
#     while f < n and a[f] < b[s]:
#         f += 1
#     s += 1
#     res.append(f)
# print(*res)


# ЗАДАЧА С Число Пар равных
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# f = 0
# s = 0
# res = 0
# while f < n and s < m:
#     curr_f = a[f]
#     curr_s = b[s]
#     cnt_f = 0
#     cnt_s = 0
#     if curr_f == curr_s:
#         while f < n:
#             if a[f] == curr_f:
#                 f += 1
#                 cnt_f += 1
#             else:
#                 break
#         while s < m:
#             if b[s] == curr_s:
#                 s += 1
#                 cnt_s += 1
#             else:
#                 break
#     elif curr_f > curr_s:
#         while s < m:
#             if b[s] <= curr_s:
#                 s += 1
#             else:
#                 break
#     elif curr_s > curr_f:
#         while f < n:
#             if a[f] <= curr_f:
#                 f += 1
#             else:
#                 break
#     res += cnt_f * cnt_s
# print(res)

# ИТМО КРУЖОК ШАГ №2
# ЗАДАЧА А
# n, s = map(int, input().split())
# a = list(map(int, input().split()))
# l = 0
# r = 0
# curr_sum = 0
# curr_len = 0
# res = 0
# while r < n:
#     curr_sum += a[r]
#     while l <= r and curr_sum > s:
#         curr_sum -= a[l]
#         l += 1
#     if curr_sum <= s:
#         curr_len = max(curr_len, r - l + 1)
#     r += 1
# print(curr_len)

# ЗАДАЧА Б
# n, s = map(int, input().split())
# a = list(map(int, input().split()))
# l = 0
# r = 0
# curr_len = float("inf")
# curr_sum = 0
# res = 0
# while r < n:
#     curr_sum += a[r]
#     while curr_sum >= s:
#         curr_len = min(curr_len, r - l + 1)
#         curr_sum -= a[l]
#         l += 1
#     r += 1
#
# if curr_len == float("inf"):
#     print(-1)
# else:
#     print(curr_len)


# ЗАДАЧА С


# # ИТМО КРУЖОК ДВА УКАЗАТЕЛЯ №1
# n, m = map(int, input().split())
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# res = []
# f = 0
# s = 0
# while f < n and s < m:
#     if arr1[f] <= arr2[s] :
#         res.append(arr1[f])
#         f += 1
#     elif arr2[s] <= arr1[f]:
#         res.append(arr2[s])
#         s += 1
# if f != n:
#     for i in arr1[f:]:
#         res.append(i)
#
# if s != m:
#     for i in arr2[s:]:
#         res.append(i)
# print(*res)

# ЗАДАЧА Б число меньших
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# res = []
# f = 0
# s = 0
#
# while s < m:
#     while f < n and a[f] < b[s]:
#         f += 1
#     s += 1
#     res.append(f)
# print(*res)


# ЗАДАЧА С Число Пар равных
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# f = 0
# s = 0
# res = 0
# while f < n and s < m:
#     curr_f = a[f]
#     curr_s = b[s]
#     cnt_f = 0
#     cnt_s = 0
#     if curr_f == curr_s:
#         while f < n:
#             if a[f] == curr_f:
#                 f += 1
#                 cnt_f += 1
#             else:
#                 break
#         while s < m:
#             if b[s] == curr_s:
#                 s += 1
#                 cnt_s += 1
#             else:
#                 break
#     elif curr_f > curr_s:
#         while s < m:
#             if b[s] <= curr_s:
#                 s += 1
#             else:
#                 break
#     elif curr_s > curr_f:
#         while f < n:
#             if a[f] <= curr_f:
#                 f += 1
#             else:
#                 break
#     res += cnt_f * cnt_s
# print(res)

# ИТМО КРУЖОК ШАГ №2
# ЗАДАЧА А
# n, s = map(int, input().split())
# a = list(map(int, input().split()))
# l = 0
# r = 0
# curr_sum = 0
# curr_len = 0
# res = 0
# while r < n:
#     curr_sum += a[r]
#     while l <= r and curr_sum > s:
#         curr_sum -= a[l]
#         l += 1
#     if curr_sum <= s:
#         curr_len = max(curr_len, r - l + 1)
#     r += 1
# print(curr_len)

# ЗАДАЧА Б
# n, s = map(int, input().split())
# a = list(map(int, input().split()))
# l = 0
# r = 0
# curr_len = float("inf")
# curr_sum = 0
# res = 0
# while r < n:
#     curr_sum += a[r]
#     while curr_sum >= s:
#         curr_len = min(curr_len, r - l + 1)
#         curr_sum -= a[l]
#         l += 1
#     r += 1
#
# if curr_len == float("inf"):
#     print(-1)
# else:
#     print(curr_len)


# ЗАДАЧА С
# n, s = map(int, input().split())
# a = list(map(int, input().split()))
# l = 0
# r = 0
# curr_sum = 0
# count = 0
# while r < n:
#     curr_sum += a[r]
#     while l <= r and curr_sum >= s:
#         curr_sum -= a[l]
#         l += 1
#     count += r - l + 1
#     r += 1
# print(count)

# ЗАДАЧА Д
# n, s = map(int, input().split())
# a = list(map(int, input().split()))
# l = 0
# r = 0
# curr_sum = 0
# res = 0
# while r < n:
#     curr_sum += a[r]
#     while l <= r and curr_sum >= s:
#         res += n - r
#         curr_sum -= a[l]
#         l += 1
#     r += 1
# print(res)

# ЗАДАЧА Е

# BAD ATTEMPT
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# unique = set()
# l = 0
# r = 0
# res = 0
# while r < n:
#     unique.add(a[r])
#     while len(unique) > k:
#         unique.clear()
#         l += 1
#         for i in range(l, r+1):
#             unique.add(a[i])
#     res += r - l + 1
#     r += 1
#
# print(res)

# ints = lambda: list(map(int, input().split()))
# n, k = ints()
# a = ints()
# q = 0
# mp = {}
# l = 0
# res = 0
# for r in range(n):
#    right = a[r]
#    if right not in mp:
#        mp[right] = 1
#        q += 1
#    else:
#        mp[right] += 1
#    while q > k:
#        left = a[l]
#        mp[left] -= 1
#        if mp[left] == 0:
#            del mp[left]
#            q -= 1
#        l += 1
#    res += r - l + 1
# print(res)


















