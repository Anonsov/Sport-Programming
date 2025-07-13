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


# m, n = map(int, input().split()) 
# k = int(input())  
# sets = {i: set() for i in range(1, n+1)}            
# element_to_sets = {i: set() for i in range(1, m+1)} 
# for _ in range(k):
#     parts = input().split()

#     if parts[0] == "ADD":
#         element = int(parts[1])
#         set_id = int(parts[2])
#         sets[set_id].add(element)
#         element_to_sets[element].add(set_id)

#     elif parts[0] == "LISTSET":
#         set_id = int(parts[1])
#         result = sorted(sets[set_id])
#         if result:
#             print(*result)
#         else:
#             print(-1)

#     elif parts[0] == "LISTSETSOF":
#         element = int(parts[1])
#         result = sorted(element_to_sets[element])
#         if result:
#             print(*result)
#         else:
#             print(-1)


# a = [1,2,6,7,8,9,45]
# b = [2,10,13,18]
# c = []
# i = 0
# j = 0
# while i < len(a) and j < len(a):
#     if i > len(a) - 1:
#         for x in b[j:]:
#             c.append(x)
#         break
#     elif j > len(b) - 1:
#         for x in a[i:]:
#             c.append(x)
#         break
#     if a[i] < b[j]:
#         c.append(a[i])
#         i += 1
#     elif b[j] < a[i]:
#         c.append(b[j])
#         j += 1
#     else:
#         c.append(a[i])
#         c.append(b[j])
#         i += 1
#         j += 1
    
#     print(f"i - {i}, j - {j}")
#     print(c)
    


