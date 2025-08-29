# Z - Функции Введение в строки
# Задача А
# def is_palindrome(curr_str: str) -> bool:
#     l = 0
#     r = len(curr_str) - 1
#     while l <= r:
#         if curr_str[l] != curr_str[r]:
#             return False
#         l += 1
#         r -= 1
#     return True


# def solve(s):
#     curr_str = s[0]
#     length = 1
    
#     for i in range(1, len(s)):
#         curr_str += s[i]
#         if is_palindrome(curr_str):
#             length = len(curr_str)
    
#     return length   
    

# t = int(input())
# for _ in range(t):
#     s = input()
#     print(solve(s))
    
    

    
# Задача B
