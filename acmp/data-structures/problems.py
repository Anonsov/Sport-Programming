# 0254
# t = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# locked = [False] * t
# for _ in range(m):
#     f, s = map(int, input().split())
#     for i in range(t):
#         if not locked[i] and arr[i] == f:
#             arr[i] = s
#             locked[i] = True
# print(*arr)


# 0385
# from math import sqrt
# t = int(input())
# all = []
# unique = set()
# for _ in range(t):
#     x, y = map(int, input().split())
#     all.append([x, y])
# for i in range(0, t):
#     for j in range(i, t):
#         if i != j:
#             x1 = all[i][0]
#             y1 = all[i][1]
#             x2 = all[j][0]
#             y2 = all[j][1]
#             result = sqrt((x2-x1)**2 + (y2-y1)**2)
#             unique.add(result)
# unique = sorted(unique)        
# unique.insert(0,len(unique))
# for i in unique:
#     print(i)


# 0946
# t = int(input())
# arr = []
# res = []
# l = 0
# r = -1
# for _ in range(t):
#     n = list(map(int, input().split()))
#     if len(n) == 2:
#         if n[0] == 1:
#             arr.insert(l, n[1])
#         elif n[1] == 2:
#             arr.append(n[1])
#     else:
#         if n[0] == 3:
#             res.append(arr[l])
#             l+=1
#         elif n[0] == 4:
#             res.append(arr[r])
#             r-=1
# print(*res)           
# arr = []
# arr.insert(0, 4)
# print(arr)


# 0262

# N,M,K = map(int, input().split())
# field = []
# for i in range(M):
#     row = list(map(int, input().split()))
#     row.append(field)
    
# rects = {}

# for i in range(N):
#     for j in range(M):
#         num = field[i][j]
#         x = j
#         y = N - 1 - i

#         if num not in rects:
#             rects[num] = [x, y, x, y]
#         else:
#             if x < rects[num][0]: rects[num][0] = x
#             if y < rects[num][1]: rects[num][1] = y
#             if x > rects[num][2]: rects[num][2] = x
#             if y > rects[num][3]: rects[num][3] = y

# for num in range(1, K + 1):
#     x1, y1, x2, y2 = rects[num]
#     print(x1, y1, x2 + 1, y2 + 1)





