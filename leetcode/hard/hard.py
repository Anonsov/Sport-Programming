# Dungeon Game
# def calculateMinimumHP(dungeon: list[list[int]]) -> int:
#     m = len(dungeon)
#     n = len(dungeon[0])
    
#     dp = [[0 for _ in range(n)] for _ in range(m)]
    
#     dp[m-1][n-1] = max(1, 1- dungeon[m-1][n-1])
#     for i in range(n-2, -1, -1):
#         dp[m-1][i] =  max(1, dp[m-1][i+1] - dungeon[m-1][i])
    
#     for i in range(m-2, -1, -1):
#         dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
    
#     for i in range(m-2, -1, -1):
#         for j in range(n - 2, -1, -1): 
#             dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
    
#     return dp[0][0]

# print(calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))





class Solution:
    def largestIsland(grid: list[list[int]]) -> int:
        n = len(grid)
        s = 0
        def dfs(i, j, p):
            nonlocal s
            s = 0  # Reset counter for each new island
            return dfs_helper(i, j, p)

        def dfs_helper(i, j, p):
            nonlocal s
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = p
            s += 1
            dfs_helper(i, j - 1, p)
            dfs_helper(i - 1, j, p)
            dfs_helper(i + 1, j, p)
            dfs_helper(i, j + 1, p)
            return s

        mp = {}
        p = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    mp[p] = dfs(i, j, p)
                    p += 1
        
        if not mp:
            return 1
        
        if len(mp) == 1:
            p -= 1
            if mp[p] == n * n:
                return mp[p]
            else:
                return mp[p] + 1
        
        mx = 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    curr = 1
                    sosed = set()

                    if i + 1 < n and grid[i + 1][j] > 1:
                        sosed.add(grid[i + 1][j])
                    
                    if i - 1 >= 0 and grid[i  - 1][j] > 1:
                        sosed.add(grid[i - 1][j])
                    
                    if j + 1 < n and grid[i][j+1] > 1:
                        sosed.add(grid[i][j + 1])
                    
                    if j - 1 >= 0 and grid[i][j - 1] > 1:
                        sosed.add(grid[i][j-1])
                    
                    for p in sosed:
                        curr += mp[p]
                    mx = max(mx, curr)
        return mx
    
a = Solution.largestIsland([[1,1],[1,0]])

print(a)