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
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
f = 0
s = 0
res = 0
while f < n and s < m:
    curr_f = a[f]
    curr_s = b[s]
    cnt_f = 0
    cnt_s = 0
    if curr_f == curr_s:
        while f < n:
            if a[f] == curr_f:
                f += 1
                cnt_f += 1
            else:
                break
        while s < m:
            if b[s] == curr_s:
                s += 1
                cnt_s += 1
            else:
                break
    elif curr_f > curr_s:
        while s < m:
            if b[s] <= curr_s:
                s += 1
            else:
                break
    elif curr_s > curr_f:
        while f < n:
            if a[f] <= curr_f:
                f += 1
            else:
                break
    res += cnt_f * cnt_s
print(res)