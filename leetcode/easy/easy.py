# Climbing Stairs
# def climbStairs(n: int) -> int:
#         dp = [0] * n
#         if n < 2:
#             return 1
#         dp[0] = 1
#         dp[1] = 2
#         for i in range(2, n):
#             dp[i] = dp[i-2] + dp[i-1]
#         return dp[n-1]

# N-th Tribonacci Number
# def tribonacci(n: int) -> int:
#         if n == 1 or n == 2:
#             return 1
#         elif n == 0:
#             return 0
#         dp = [0] * (n + 1)
        
#         dp[1] = 1
#         dp[2] = 1
        
#         for i in range(3, n + 1):
#             dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        
#         return dp[n]


# Min Cost Climbing Stairs
# def minCostClimbingStairs(cost: list[int]) -> int:
#     length = len(cost)
#     dp = [0] * length
#     dp[0] = cost[0]
#     dp[1] = cost[1]
    
#     for i in range(2, length):
#         mn = min(dp[i - 2], dp[i - 1])
#         dp[i] = mn + cost[i]
    
#     return min(dp[-1], dp[-2])

# print(minCostClimbingStairs([10,15,20]))
