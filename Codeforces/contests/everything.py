# # a
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     if n % 4 == 0:
#         print("Bob")
#     else:
#         print("Alice")
        
# t = int(input())

# for _ in range(t):
#     n, j, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     cur = a[j-1]
#     x = 0
#     for i in a:
#         if i > cur:
#             x += 1
    
#     if x <= n - k:
#         print("YES")
#     else:
#         print("NO")
        
# t = int(input())
# for _ in range(t):
#     n = input()
#     print(min(n))

# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     curr_summ = sum(arr[:k])
#     l = 0
#     i = k
#     res = 0
#     while i < n:
#         if curr_summ >= 1:
#             if i < n:
#                 curr_summ += arr[i]
#             curr_summ -= arr[l]
#             l += 1
#             i += 1
#         elif curr_summ == 0:
#             l += k
#             i += k
#             if i <= n:
#                 curr_summ = sum(arr[l:i])
#             res += 1
#     print(res)



# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     pref = [0] * (n + 1)
#     for i in range(n):
#         pref[i+1] = pref[i] + a[i]
#
#     res = 0
#     i = 0
#     while i <= n - k:
#         if pref[i+k] - pref[i] == 0:
#             res += 1
#             i += k + 1
#         else:
#             i += 1
#     print(res)