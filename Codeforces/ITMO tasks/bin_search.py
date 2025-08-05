
# ---------------------------------
# ИТМО ШАГ 1 БИН ПОИСК
# ---------------------------------
# ИТМО кружок контесты бин поиск 1
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# q = list(map(int, input().split()))
#
# def binary_search(arr, i):
#     l = 0
#     r = len(arr) - 1
#
#     while l <= r:
#         mid = (l + r) // 2
#         if arr[mid] == i:
#             return True
#         elif arr[mid] > i:
#             r = mid - 1
#         else:
#             l = mid + 1
#     return False
#
#
# for i in q:
#     found = binary_search(arr, i)
#     if found:
#         print("YES")
#     else:
#         print("NO")



# ИТМО кружок контесты бин поиск 2
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# q = list(map(int, input().split()))
#
# for i in range(k):
#     l = -1
#     r = n - 1
#     while l < r:
#         mid = (l + r + 1) // 2
#         if arr[mid] <= q[i]:
#             l = mid
#         else:
#             r = mid - 1
#
#     if l == -1:
#         print(0)
#     else:
#         print(l + 1)

# ИТМО кружок контесты бин поиск 3
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# q = list(map(int, input().split()))
#
# for i in range(k):
#     l = 0
#     r = n
#     while l < r:
#         mid = (l + r) // 2
#         if arr[mid] < q[i]:
#             l = mid + 1
#         else:
#             r = mid
#     print(r + 1)

# ИТМО кружок контесты бин поиск 4 - БЛЯТЬ Я ПОНЯЛ КАК ЭТО ДЕЛАЕТСЯ ЕПТА
# n = int(input())
# arr = list(map(int, input().split()))
# arr = sorted(arr)
# k = int(input())
# res = []
# for i in range(k):
#     l, r = map(int, input().split())
#     left1 = 0
#     right1 = n
#     while left1 < right1:
#         mid = (left1 + right1 + 1) // 2
#         if arr[mid] < l:
#             left1 = mid
#         else:
#             right1 = mid - 1
#     if left1 == -1:
#         left1 = 0
#     elif arr[left1] < l:
#         left1 += 1
#     left2 = 0
#     right2 = n
#     while left2 < right2:
#         mid = (left2 + right2) // 2
#         if arr[mid] <= r:
#             left2 = mid + 1
#         else:
#             right2 = mid
#     res.append(right2 - left1)
#     # print(right2, left1)
# print(*res)

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# k = int(input())
# res = []
#
# for i in range(k):
#     l, r = map(int, input().split())
#
#     left = 0
#     right = n
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] >= l:
#             right = mid
#         else:
#             left = mid + 1
#     pos1 = left
#
#     left = 0
#     right = n
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] > r:
#             right = mid
#         else:
#             left = mid + 1
#     pos2 = left
#
#     res.append(pos2 - pos1)
#
# print(*res)



# ---------------------------------
# ИТМО ШАГ 2 БИН ПОИСК
# ---------------------------------
# ИТМО КРУЖОК БИН ПОИСК #1

# w, h, n = map(int, input().split())
# l = max(w, h)
# r = 10 ** 18
# while l < r:
#     m = (l + r) // 2
#     rectangles_fit = (m // w) * (m // h)
#     if rectangles_fit >= n:
#         r = m
#     else:
#         l = m + 1
# print(l)


# n, k = map(int,input().split())
# a = [int(input()) for _ in range(n)]
# l = 0
# r = 1e8
# for i in range(100):
#     s = 0
#     m = (l + r) / 2
#     for j in range(n):
#         s += a[j] // m
#     if s >= k:
#         l = m
#     else:
#         r = m
# print(f"{l:.6f}")

#
# n, x, y = map(int, input().split())
#
# def solve(time):
#     if n == 0:
#         return True
#
#     if time < min(x,y):
#         return False
#
#     cnt = 1 + ((time - min(x,y)) // x) + ((time - min(x,y)) // y)
#     return cnt >= n
#
# l = 0
# r = 10**10
# while l < r:
#     m = (l + r) // 2
#     if solve(m):
#         r = m
#     else:
#         l = m + 1
#
# print(l)


# m, n = map(int, input().split())
# mat = []
# for i in range(n):
#     temper = list(map(int, input().split()))
#     mat.append(temper)
#
# def checker(s):
#     rt = 0
#     if m == 0:
#         return True
#
#     for i in range(n):
#         t, z, y = mat[i]
#         rt += (s // t)
#
#     return rt






