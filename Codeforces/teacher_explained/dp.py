# Задача Зайчика - done
# def dp_first(n, k):
#     dp = [0]*(n+1)
#     k_counter = 1
#     sdp = 0
#     while k_counter <= k:
#         sdp += dp[k_counter - 1]
#         dp[k_counter] = sdp + 1
#         k_counter += 1
#     sdp += dp[k]
#     counter = 1
#     for i in range(k+1, n + 1):
#         dp[i] = sdp
#         sdp -= dp[counter]
#         sdp += dp[i]
#         counter += 1
#     print(sdp)
        
# dp_first(5, 2)
        
        
# Задача белки
# from random import randint
# def solve(n, m):
#     matrix = []
#     for _ in range(n):
#         row = [randint(10, 30) for _ in range(m)]
#         matrix.append(row)
    
#     dp_matrix = []
#     for l in range(n):
#         row = [0]*m
#         dp_matrix.append(row)
            
#     sh = 0
#     for i in range(m):
#         sh += matrix[0][i]
#         dp_matrix[0][i] = sh
        
    
#     sv = 0
#     for i in range(n):
#         sv += matrix[i][0]
#         dp_matrix[i][0] = sv
        
        
#     for i in range(1, n):
#         for j in range(1, m):
#             dp_matrix[i][j] = max(dp_matrix[i-1][j], dp_matrix[i][j-1]) + matrix[i][j]
        
#     for l in dp_matrix:
#         print(*l)
        
# solve(5,4)
    
    
# Задача с номиналами 
# def solve(n: int, a: list):
#     max_sum = sum(a)
#     dp_matrix = []
#     dp_matrix = []
#     for _ in range(n+1):
#         dp_matrix.append([False]*(max_sum+1))
    
#     for i in range(n+1):
#         dp_matrix[i][0] = True
    
#     for i in range(1, max_sum):
#         dp_matrix[0][i] = False
    
    
#     for i in dp_matrix:
#         print(*i)
    
#     possible_sums = []
#     for j in range(1, max_sum+1):
#         if dp_matrix[n][j]:
#             possible_sums.append(j)
            
#     return possible_sums



# print(solve(3, [2,2,3]))



     
# n = int(input())
# dp = []
# for i in range(10):
#     row = []
#     for j in range(n+1):
#         row.append(0)
#     dp.append(row)


# for j in range(1, 10):
#     dp[j][1] = 1
    
    
# for j in range(2, n + 1):
#     for i in range(10):
#         if i > 0:
#             dp[i][j] += dp[i-1][j-1]
#         dp[i][j] += dp[i][j-1]
#         if i < 9:
#             dp[i][j] += dp[i+1][j-1]     
            
# res = 0
# for i in range(10):
#     res += dp[i][n] 

# print(res)  