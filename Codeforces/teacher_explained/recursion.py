# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(5))

# def rec(n):
#     if n == 0:
#         return 1
#     rec(n-1)
#     print(n)

# rec(5)

# def make_palindrome(s):
#     if len(s) == 0:
#         return ""
#     return s[-1] + make_palindrome(s[:-1]) 

# print(make_palindrome("hello"))


# def sdigits(s):
#     if s == 0:
#         return 0
#     # print(s)
#     return s % 10 + sdigits(s // 10)
    
# print(sdigits(12345))

# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
   
#     return is_palindrome(s[1:-1])

# print(is_palindrome("helloh"))
# cnt = 0
# def count_symbols(s, c):
#     global cnt
#     if len(s) == 0:
#         return cnt
#     if s[-1] == c:
#         cnt += 1
#     return count_symbols(s[:-1], c)


# print(count_symbols("banana", "a"))
# f = ""
# def del_symbol(s: str, c: str) -> str:
#     global f
#     if len(s) == 0:
#         return f
#     if s[0] != c:
#         f += s[0]
#     return del_symbol(s[1:], c)

# print(del_symbol("hello", "l"))
# s = 0
# def sum_elem_arr(a: list, i) -> int:
#     global s
#     if i == len(a):
#         return s
#     s += a[i]
#     return sum_elem_arr(a, i + 1)

# print(sum_elem_arr([1,2,3,4,5], 0))
    
# mx = float('-inf')
# def find_max(a: list, i):
#     global mx
#     if i == len(a):
#         return mx
#     if a[i] >= mx:
#         mx = a[i]
    
#     return find_max(a, i + 1)    
# print(find_max([3, 1, 4, 1, 5, 9], 0))


# def binary_search_rec(a: list, l: int, r: int, f: int) -> bool:
#     if l > r:
#         return -1
#     m = (l + r) // 2
#     if a[m] == f:
#         return m
#     elif a[m] < f:
#         return binary_search_rec(a, m + 1, r, f)
#     else:
#         return binary_search_rec(a, l, m - 1, f)

# print(binary_search_rec([1, 3, 5, 7, 9, 11, 13], 0, 6, 5))

# def quick_sort():
#     pass

# def solve():
#     pass

# def generate(a: list, i, curr_a):
#     if i == len(a):
#         print(curr_a)
#         return
#     generate(a, i + 1, curr_a)
#     curr_a.append(a[i])
#     generate(a, i + 1, curr_a)
#     curr_a.pop()
    
# generate([1,2,3],0,[])
    

# def solve(w, t, i=0):
#     if t == 0:
#         return 1
#     if t < 0 or i >= len(w):
#         return 0
    
#     cnt = 0
#     cw = w[i]
    
#     mx_cnt = t // cw
#     for j in range(mx_cnt + 1):
#         r = t - j * cw
#         cnt += solve(w, r, i + 1)
        
#     return cnt

# X, Y, Z, W = map(int, input().split())
# result = solve([X, Y, Z], W)
# print(result)


# Hanoi
# def hanoi(n, fr, to, temp):
#     if n > 0:
#         hanoi(n - 1, fr, temp, to)
#         print(fr, "->", to)
#         hanoi(n - 1, temp, to, fr)
        
# hanoi(3, 'A', 'B', 'C')

