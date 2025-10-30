
# Perfect Square
# from math import sqrt
# def solve(n):
#     dp = [0] * (n + 1)
#     p = []
    
#     for i in range(1, int(sqrt(n)) + 1):
#         p.append(i ** 2)
#         dp[i**2] = 1
        
#     # print(p)
    
#     np = len(p)
#     for i in range(1, n + 1):
#         mn = float('inf')
#         for j in range(np):
#             if dp[i] != 1:
#                 if p[j] <= i:
#                     mn = min(mn, dp[i - p[j]] + 1)
#                 else:
#                     break
#                 dp[i] = mn
    
#     print(dp[n])
# solve(1)
    
# House Robber
# def rob( nums: list[int]) -> int:
#     dp = [0] * len(nums)
#     if len(nums) < 2:
#         return max(nums)
#     dp[0] = nums[0]
#     dp[1] = max(nums[0], nums[1])
#     for i in range(2, len(nums)):
#         dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
#     return max(dp[-1], dp[-2])

# Decode Ways
# def numDecodings(s: str) -> int:
#     dp = [0] * (len(s) + 1)
#     dp[0] = 1
#     for i in range(1, len(s) + 1):
#         if s[i-1] != '0':
#             dp[i] += dp[i - 1]
#         if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
#             dp[i] += dp[i-2]
    
#     return dp

# print(numDecodings("121"))
# print(numDecodings("101"))


# Minimum Cost For Tickets
# def mincostTickets(days: list[int], costs: list[int]) -> int:
#     dp = [0] * (days[-1] + 1)
#     set_days = set(days)
#     for i in range(1, len(dp)):
#         if i in set_days:
#             dp[i] = min(
#                 dp[i - 1] + costs[0],
#                 dp[max(0, i - 7)] + costs[1],
#                 dp[max(0, i - 30)] + costs[2]
#             )
#         else:
#             dp[i] = dp[i-1]
#     return dp

# print(mincostTickets(
#     [1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29],
#     [3,14,50]
#     ))


# Solving Questions With Brainpower
# def mostPoints(questions: list[list[int]]) -> int:
#     n = len(questions)
#     dp = [0] * (n + 1)
#     for i in range(n-1, -1, -1):
#         points, brainpowers = questions[i]
#         dp[i] = max(
#             dp[min(n, i + brainpowers + 1)] + points,
#             dp[i+1]
#         )
#     return dp[0]
    
# print(mostPoints([[3,2],[4,3],[4,4],[2,5]]))


# Unique Paths

# def uniquePaths(m: int, n: int) -> int:
#     dp_matrix = []
#     for _ in range(m):
#         row = [0] * n
#         dp_matrix.append(row)
    
#     for i in range(n):
#         dp_matrix[0][i] = 1
    
#     for i in range(m):
#         dp_matrix[i][0] = 1
    
#     for i in range(1, m):
#         for j in range(1, n):
#             dp_matrix[i][j] = dp_matrix[i-1][j] + dp_matrix[i][j-1]
    
#     return dp_matrix[-1][-1]

# print(uniquePaths(3, 7))


# Unique Paths II
# def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
#     m = len(obstacleGrid)
#     n = len(obstacleGrid[0])
#     if obstacleGrid[0][0] == 1:
#         return 0
    
#     dp = [[0 for _ in range(n)] for _ in range(m)]
#     dp[0][0] = 1
    
#     for j in range(1, n):
#         if obstacleGrid[0][j] == 0:
#             dp[0][j] = dp[0][j-1]
    
#     for i in range(1, m):
#         if obstacleGrid[i][0] == 0:
#             dp[i][0] = dp[i-1][0]
                
#     for i in range(1, m):
#         for j in range(1, n):
#             if obstacleGrid[i][j] == 0:
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
#     return dp[m-1][n-1]
# print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))

# Minimum Path Sum
# def minPathSum(grid: list[list[int]]) -> int:
#     m = len(grid)
#     n = len(grid[0])
#     dp = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             row.append(0)
#         dp.append(row)
#     print(dp)
#     dp[0][0] = grid[0][0]
#     print(dp)
    
#     for i in range(1, n):
#         dp[0][i] = dp[0][i-1] + grid[0][i]
    
#     for j in range(1, m):
#         dp[j][0] = dp[j-1][0] + grid[j][0]
    
#     for i in range(1, m):
#         for j in range(1, n):
#             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            
            
#     return dp[m-1][n-1]

# print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))


# Count Square Submatrices with All Ones
# def countSquares(matrix: list[list[int]]) -> int:
#     if not matrix or not matrix[0]:
#         return 0
    
#     m = len(matrix)
#     n = len(matrix[0])
#     dp = [[0] * n for _ in range(m)]
    
#     cnt = 0
    
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] == 1:
#                 if i == 0 or j == 0:
#                     dp[i][j] = 1
#                 else:
#                     dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
#                 cnt += dp[i][j]
#     return dp

# print(countSquares([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

# Maximal Square
# def maximalSquare(matrix: list[list[str]]) -> int:
    # if matrix is None or len(matrix) < 1:
    #     return 0
    
    # m = len(matrix)
    # n = len(matrix[0])
    # dp = [[0]*(n+1) for _ in range(m+1)]
    # max_side = 0
    # for i in range(m):
    #     for j in range(n):
    #         if matrix[i][j] == "1":
    #             dp[i+1][j+1] = min(
    #                 dp[i][j], dp[i + 1][j], dp[i][j+1]
    #             ) + 1
    #             max_side = max(max_side, dp[i+1][j+1])
    
    # return max_side * max_side 

# def searchMatrix(matrix: list[list[int]], target: int) -> bool:
#     n = len(matrix)
#     m = len(matrix[0])
    
#     for i in range(n):
#         l = 0
#         r = m - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if matrix[i][mid] == target:
#                 return True
#             elif matrix[i][mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#     return False

# print(searchMatrix(
#     [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3
# ))

# from typing import List
# def setZeroes(matrix: List[List[int]]) -> None:
#     """
#     Do not return anything, modify matrix in-place instead.
#     """
#     flag = float('inf')
#     n = len(matrix)
#     m = len(matrix[0])
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 if i + 1 >= n:
#                     matrix[0][j] = flag
#                 else:
#                     matrix[i + 1][j] = flag

#                 if j + 1 >= m:
#                     matrix[i][0] = flag
#                 else:
#                     matrix[i][j + 1] = flag
#                 matrix[i - 1][j] = flag
#                 matrix[i][j - 1] = flag
#                 matrix[i][j] = flag
#     for i in matrix:
#         print(i)

        
# setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])


def simplifyPath(path: str) -> str:
    
    """
    как то нужно использовать stack чтобы проверять, допустим две точки, значит выходим, если одна точка то нужно остаться и ничего не делать, если слешов много то скипать их, может быть мне нужно будет использовать сплит функцию, идея пока что такова
    """
    # def slash_passer(path, i):
    #     while i < len(path) and path[i] == "/":
    #         i += 1
    #     return i
    
    # def dot_passer(path, i):
    #     cnt = 0
    #     while i < len(path) and path[i] == ".":
    #         cnt += 1
    #         i += 1
    #     return [cnt, i]
    # def get_word_until_slash(path, i):
    #     res = ""
    #     while i < len(path) and (path[i] != "/" and path[i] != "."):
    #         res += path[i]
    #         i += 1
    #     return [res, i]

    # stack = []
    # i = 0
    # ans = "/"
    # while i < len(path):
    #     if path[i] == "/":
    #         i = slash_passer(path, i)
    #     elif path[i] == ".":
    #         res = dot_passer(path, i)
    #         cnt = res[0]
    #         i = res[-1]
    #         if cnt == 1:
    #             continue
    #         elif cnt == 2 and stack:
    #             stack.pop()
    #         elif cnt > 2:
    #             stack.append(cnt * ".")
    #     else:
    #         res = get_word_until_slash(path, i)
    #         word = res[0]
    #         i = res[-1]
    #         stack.append(word +"/")
    # for i in range(len(stack)):
    #     ans+=stack[i]
    # if len(ans) == 1:
    #     print(ans)
    # else:
    #     print(ans[:-1])
        
# simplifyPath("/../")
# simplifyPath("/home/user/Documents/../Pictures")
# simplifyPath("/.../a/../b/c/../d/./")
# simplifyPath("/home/")
# simplifyPath("/a//b////c/d//././/..")


