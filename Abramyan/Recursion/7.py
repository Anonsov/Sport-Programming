# def c2(n, k):
#     global grid
#     if n == k or k == 0:
#         return 1
#     if grid[n][k] == 0:
#         grid[n][k] = c2(n - 1, k) + c2(n -1, k-1)
#     return grid[n][k]
    
# n = 4
# k= 2    
# grid = []
# for i in range(n+1):
#     row = []
#     for j in range(k+1):
#         row.append(0)
#     grid.append(row)
# print(c2(n, k))