# 498 K-перестановки


# def k_permutations(curr, mpc, n, k):

#     if len(curr) == n:
#         return 1
#     cnt = 0
#     for i in range(1, n + 1):
#         if not mpc[i]:
#             if len(curr) == 0 or abs(i - curr[-1]) <= k:
#                 mpc[i] = True
#                 curr.append(i)
#                 cnt += k_permutations(curr, mpc, n, k)
#                 curr.pop()
#                 mpc[i] = False
#     return cnt
    
# n, k = map(int, input().split())
# mpc = [False] * (n + 1)
# print(k_permutations([], mpc, n, k))


