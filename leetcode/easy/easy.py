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


# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         res_str = ""
#         ost = 0
#         i = len(num1) - 1
#         j = len(num2) - 1
#         c = 0
#         res = []
#         while i >=0 or j >= 0 or c:
#             if i >= 0:
#                 dg = int(num1[i])
#             else:
#                 dg = 0
            
#             if j >= 0:
#                 dg2 = int(num2[j])
#             else:
#                 dg2 = 0
            
#             t = dg + dg2 + c
#             c = t // 10
#             res.append(str(t % 10))
            
#             i-=1
#             j-=1
        
#         for i in range(len(res) - 1, -1 , -1):
#             res_str += res[i]
        
#         return res_str

# class Solution:
#     def maxPower(self, s: str) -> int:
#         res = 0
#         l = 0
#         r = 0
#         mx = float('-inf')
#         while l < len(s) and r < len(s):
#             if s[r] == s[l]:
#                 r += 1
#                 res += 1
#             else:
#                 l = r
#                 res = 0
#             mx = max(mx, res)
#         return mx

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         mp = {}
#         for i in range(len(s)):
#             if s[i] in mp:
#                 mp[s[i]] += 1
#             else:
#                 mp[s[i]] = 1
            
#         for i in range(len(s)):
#             if mp[s[i]] == 1:
#                 return i
#         return -1


# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     i = 0
#     l = 0
#     r = 0
    
# from typing import List
# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     i = m - 1
#     j = n - 1
#     k = n + m - 1
    
#     while j >= 0:
#         if i >= 0 and nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i-=1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k-=1
        
#     return nums1    
# print(merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5))
# from typing import List
# def canJump(nums: List[int]) -> bool:
#     dp = [False] * len(nums)
#     dp[0] = True
#     if len(nums) == 1:
#         return True
#     i = 0
#     mx = nums[0]
#     while i < len(nums) - 1:
#         mx = max(mx, i + nums[i])
#         if i >= mx:
#             return False
        
#         i += 1
#     return True

# print(canJump([2,3,0,3,0,0,1,0]))

