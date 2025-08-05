# 266A

# a = int(input())
# st = input()
# k = 0
# for i in range(0, len(st) - 1):
#     if st[i] == st[i+1]:
#         k += 1

# print(k)



# 118A

# a = "aoyeui"
# s = input().lower()
# res = ""
# for i in range(0, len(s)):
#     if s[i] not in a:
#         res+="." + s[i]
# print(res)


# 58A
# s = input()
# hello = "hello"
# x = 0
# for i in s:
#     if i == hello[x]:
#         x += 1
#         if x == len(hello):
#             break

# if x == len(hello):
#     print("YES")
# else:
#     print("NO")
        
        
# 467A
# n = int(input())
# x = 0
# for i in range(n):
#     p, q = map(int, input().split())
#     if q - p >= 2:
#         x += 1

# print(x)    


# 266B

# n, sec = map(int, input().split())
# st = list(input())
# print(st)
# for i in range(0, n-1):
#     if st[i] == "B" and st[i+1] != "B":
#         st[i+sec] = "B"
#         st[i] = "G"

# print(st)


# n, sec = map(int, input().split())
# st = list(input())

# for _ in range(sec):
#     for i in range(n - 1):
#         if st[i] == "B" and st[i + 1] == "G":
#             st[i], st[i + 1] = st[i + 1], st[i]
#             i += 1  

# st = "".join(st)
# print(st)


# 344A
# n = int(input())
# res = 0
# prev = ""
# for i in range(0, n):
#     p = input()
#     if prev != p:
#         res += 1
#     prev = p
# print(res)


# 160A
# a = int(input())
# arr = list(map(int, input().split()))

# arr.sort(reverse=True)
# total_sum = sum(arr)
# current_sum = 0
# count = 0

# for coin in arr:
#     current_sum += coin
#     count += 1
#     if current_sum > total_sum - current_sum:
#         break

# print(count)

# 318A

# n, k = map(int, input().split())

# if k <= (n + 1) // 2:
#     print(2*k - 1)
# elif k > (n+1) // 2:
#     print(2 * (k - (n+1) // 2))

# a = "aabcvc"
# print(set(a))

# a = "abca"
# res = {}

# 1703B


# t = int(input())

# for i in range(t):
#     summ = 0
#     map_counter = {}
#     n = int(input())
#     s = input()
#     seen = set()
#     for j in s:
#         if j in seen:
#             summ += 1
#         else:
#             summ += 2
#             seen.add(j)
    
#     print(summ)
    
# 1760C

# t = int(input())
# for i in range(t):
#     n = int(input())
#     s = list(map(int, input().split()))
#     maximum1 = max(s)
#     indmax = s.index(maximum1)
#     maximum2 = max(s[:indmax] + s[indmax + 1:])
#     for i in s:
#         if i < maximum1:
#             print(i - maximum1)
#         else:
#             print(i - maximum2)
            

# 1722C
# 
# 
# 
# 


# 1714B
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     res = {}
#     index = 0
#     for i in range(0, n):
#         if a[i] in res:
#             res[a[i]] += 1
#         else:
#             res[a[i]] = 1
#     for i in range(0, n):
#         if res[a[i]] != 1:
#             index = i + 1
#             res[a[i]] -= 1
#     if len(set(a)) == len(a):
#         print(0)
#     else:
#         print(index)
        
        
# 1690C

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     start = list(map(int, input().split()))
#     end = list(map(int, input().split()))   
#     result = []
#     d = end[0] - start[0]
#     print(d, end=" ")
#     for i in range(0, n - 1):
#         if end[i] > start[i+1]:
#             start[i+1] = end[i]
#             result.append(abs(start[i + 1] - end[i + 1]))
#         else:
#             result.append(abs(start[i + 1] - end[i + 1]))
    
#     print(" ".join(map(str, result)))
        
# 1730A

# t = int(input())
# for _ in range(t):
#     map_counter = {}
#     tgp = 0
#     n, c = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for i in range(0, n):
#         if arr[i] in map_counter:
#             map_counter[arr[i]] += 1
#         else:
#             map_counter[arr[i]] = 1
    
#     for j in map_counter.values():
#         if c <= j:
#             tgp += c
#         elif j < c:
#             tgp += j % c
    
#     print(tgp)


# 1767B
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     x = arr[0]
#     arr = sorted(arr[1:])
#     for j in range(0, n - 1):
#         if x < arr[j]:
#             x += (arr[j] - x + 1) //2
#     print(x)
    
    
# contest

# t = int(input())
# for _ in range(t):
#     summ = 0
#     arr = list(map(int, input().split()))


# def main():
#     l1, b1, l2, b2, l3, b3 = map(int, input().split())
#     if l1 > b1:
#         if l1 == b1 + b2 + b3 and l1 == l2 == l3:
#             return "YES"
#         if l1 == b1 + b2 and b2 == b3 and l1 == l2 + l3:
#             return "YES"
#     else:
#         if b1 == b2 == b3 and b1 == l1 + l2 + l3:
#             return "YES"
#         if b2 + b3 == b1 and l2 == l3 and l1 + l2 == b1:
#             return "YES"
#     return "NO"


# for _ in range(int(input())):
#     print(main())



# t = int(input())  

# for _ in range(t):
#     n = int(input())  
#     p1 = input().split()
#     p2 = input().split()
#     p3 = input().split()
#     p = p1 + p2 + p3
#     map_counter = {}
#     for word in p:
#         map_counter[word] = map_counter.get(word) + 1

#     s1 = 0
#     s2 = 0
#     s3 = 0

#     for word in p1:
#         if map_counter[word] == 1:
#             s1 += 3
#         elif map_counter[word] == 2:
#             s1 += 1

#     for word in p2:
#         if map_counter[word] == 1:
#             s2 += 3
#         elif map_counter[word] == 2:
#             s2 += 1

#     for word in p3:
#         if map_counter[word] == 1:
#             s3 += 3
#         elif map_counter[word] == 2:
#             s3 += 1
#     print(s1, s2, s3)



# def main():
#     input()
#     a = sorted(list(map(int, input().split())))
#     return a[-1] + a[-2] - a[0] - a[1]



# for _ in range(int(input())):
#     print(main())

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr = sorted(arr)
#     res = arr[-1] + arr[-2] - arr[0] - arr[1]
#     print(res)


# 1956A
# t = int(input())
# for _ in range(t):
#     k, q = map(int, input().split())
#     z = sorted(list(map(int, input().split())))
#     ai = list(map(int, input().split()))
#     z = z[0]
#     res = 0
#     for i in ai:
#         if i >= z:
#             print(min(i, z) - 1)
#         else:
#             print(i)

# 1200A

# n = int(input())
# a = input()
# res = [0] * 10
# for i in a:
#     if i == "L":
#         for x in range(10):
#             if res[x] == 0:
#                 res[x] = 1
#                 break
#     elif i == "R":        
#         for x in range(-1, -11, -1):
#             if res[x] == 0:
#                 res[x] = 1
#                 break
#     else:
#         res[int(i)] = 0
        
# print("".join(map(str, res)))


# 2021A
# import math
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = sorted(list(map(int, input().split())))
#     while len(arr) > 2:
#         min = sorted(arr)[0]
#         max = sorted(arr)[-2]
#         arr[-2] = math.floor((max+min) / 2)
#         arr = arr[1:]

        
#     print(math.floor((arr[0] + arr[1]) / 2))
    
    
    
# 1870D
# t = int(input())
# for _ in range(t):
#     n, ai = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for _ in range(ai):
#         l, r, k = map(int, input().split())
#         res = {"chet":0, "nechet": 0}
#         for i in range(0, l - 1):
#             if arr[i] % 2 == 0:
#                 res["chet"] += 1
#             else:
#                 res["nechet"] += 1
#         for i in range(r, n):
#             if arr[i] % 2 == 0:
#                 res["chet"] += 1
#             else:
#                 res["nechet"] += 1
#         if k % 2 == 0:
#             res["chet"] += abs(l - r) + 1
#         else:
#             res["nechet"] += abs(l - r) + 1
            
#         if res["nechet"] % 2 == 0:
#             print("NO")
#         else:
#             print("YES")
        
# t = int(input())
# for _ in range(t):
#     n, ai = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for _ in range(ai):
#         l, r, k = map(int, input().split())
#         x1 = sum(arr[:l-1]) % 2 == 0
#         # print(sum(arr[:l-1]), arr[:l-1])
#         x2 = (((r - l) + 1) * k) % 2 == 0
#         # print(((r - l) + 1) * k)
#         x3 = sum(arr[r:]) % 2 == 0
#         # print(sum(arr[r:]), arr[r:])
#         if (x1 + x2 + x3) % 2 != 0:
#             print("NO")
#         else:
#             print("YES")
            

# 282A

# n = int(input())  
# x = 0 
# for _ in range(n):
#     s = input()  
#     if "++" in s:
#         x += 1 
#     elif "--" in s:
#         x -= 1 

# print(x)
            
# s ="konjac"

# print(s[0].upper() + s[1:])


# 381A

# def func(n, arr):
#     print(arr)
#     s = 0
#     d = 0
#     z = n - 1
#     w = n - 2
#     if n == 1:
#         return [arr[0], 0]
#     while z >= 0 or w >= 0:
#         if z >= 0:
#             s += arr[z]
#             z-=2
#         if w >= 0:
#             d += arr[w]
#             w-=2
#     return [s, d]    
    
# n = int(input())
# arr = sorted(list(map(int, input().split())))
# print(*func(n, arr))
    
# 381A
# n = int(input())
# arr = list(map(int, input().split()))
# serega = 0
# dima = 0
# l = 0
# r = n - 1
# k = 0
# while r - l >= 0:
#     if k % 2 == 0:
#         if arr[l] > arr[r]:
#             serega += arr[l]
#             l += 1
#         else:
#             serega += arr[r]
#             r -= 1
#     else:
#         if arr[l] > arr[r]:
#             dima += arr[l]
#             l += 1
#         else:
#             dima += arr[r]
#             r -= 1
#     k += 1
# print(serega, dima)
    
    
# 1791C
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     res = []
#     l = 0
#     r = n - 1
#     while l <= r:
#         if l == r:
#             res.append(arr[l])
#             break
        
#         res.append(arr[l])
#         res.append(arr[r])
#         l += 1
#         r -= 1
#     print(*res)

# 1873D
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     s = input()
#     cnt = 0
#     i = 0
#     while i < n:
#         if s[i] == "B":
#             i += k
#             cnt += 1
#         else: 
#             i += 1
#     print(cnt)    


# 2000B
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     l = arr[0]
#     r = arr[0]
#     res = "YES"
#     for i in range(1,n):
#         if arr[i] + 1 == l:
#             l = arr[i]
#         elif arr[i] - 1 == r:
#             r = arr[i]
#         else:
#             res = "NO"
#             break            
#     print(res)
           
# 1840A 
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = input()
#     res = ""
#     symbol = a[0]
#     l = 0
#     r = 1
#     while l < n and r < n:
#         if a[l] == a[r]:
#             res += a[l]
#             l = r + 1
#             r = l + 1
#         else:
#             r += 1  
#     print(res)

# 1843A
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = sorted(list(map(int, input().split())))
#     l = 0
#     r = n - 1
#     res = 0
#     while l <= r:
#         res += arr[r] - arr[l]
#         l += 1
#         r -= 1
#     print(res)


# 1851B
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = sorted(a)
#     res = True
#     for i in range(n):
#         if (a[i] % 2 == 0 and b[i] % 2 == 0) or (a[i] % 2 != 0 and b[i] % 2 != 0):
#             continue
#         else:
#             res = False
#             break
#     if res:
#         print("YES")
#     else:
#         print("NO")


# 1843B
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     summ = 0
#     i = 0
#     l = 0
#     r = 0
#     cnt = 0
#     found = False
#     while i < n:
#         if a[i] == 0:
#             i+=1
#             continue
#         elif a[i] < 0:
#             if not found: 
#                 l = i
#                 cnt += 1
#                 found = True
#             r = i   
#         else:
#             found = False
#         summ += abs(a[i])    
#         i += 1
#     print(summ, cnt)

# 1968B
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     a = input()
#     b = input()
#     i = 0
#     j = 0
#     k = 0
#     while i < n and j < m:
#         if a[i] == b[j]:
#             k += 1
#             i += 1
#             j += 1
#         elif a[i] != b[j]:
#             j += 1
#     print(k)

# 2025A - not done yet
# t = int(input())
# for _ in range(t):
#     s = input()
#     t = input()
#     ls = len(s)
#     lt = len(s)
#     i = 0
#     j = 0
#     cnt = 0
#     while i < ls and j < ls:
#         if s[i] == t[j]:
#             cnt += 1
#         else:
#             break
#     if cnt == ls or cnt == lt:
#         print(cnt + 1)
#     elif cnt > 0:
#         print(cnt + 1)
        
        


# 1646B - not done yet
# --------------------- WRONG ONE-----------------------------
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr = sorted(arr, reverse=True)
#     if n % 2 == 0:
#         mid = (n // 2) - 1
#         s_summ = sum(arr[mid:])
#     else:
#         mid = n // 2
#         s_summ = sum(arr[mid:])
#     l = 0
#     k_sum = 0
#     while l < mid:
#         k_sum += arr[l]
#         l += 1
#     print(arr)
#     print(k_sum, s_summ)
#     print( k_sum + arr[mid-1], s_summ - arr[mid-1])
#     if k_sum > s_summ or (s_summ - arr[mid]) > (k_sum + arr[mid-1]):
#         print("YES")
#     else:
#         print("NO")
# --------------------- WRONG ONE-------------------------------


# 1646B
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     l = 0
#     r = n - 2
#     arr = sorted(arr, reverse=True)
#     redsumm = 0
#     bluesumm = arr[-1]
#     found = False
#     while l < r:
#         redsumm += arr[l]
#         bluesumm += arr[r]
#         if redsumm > bluesumm:
#             found = True
#             break
#         l += 1
#         r -= 1
#     if found:
#         print("YES")
#     else:
#         print("NO")

# 1746B
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = sorted(a)
#     c = 0
#     for i in range(n):
#         if a[i] != b[i]:
#             c += 1
#     print(int(c/2))


# eval()
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for o in range(m):
#         operator, l, r = map(int, input().split())
#
# for i in range()
# int(input())

# 2007B
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     maxim = max(arr)
#     res = []
#     for i in range(m):
#         operator, l, r = input().split()
#         l = int(l)
#         r = int(r)
#         if l <= maxim <= r:
#             if operator == '+':
#                 maxim += 1
#             else:
#                 maxim -= 1
#         res.append(maxim)
#     print(*res)

# 2000C
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     m = int(input())
#     for i in range(m):
#         map_counter = {}
#         map_counter2 = {}
#         # set_counter = set()
#         s = input()
#         found = True
#         if len(s) != n:
#             found = False
#         else:
#             for j in range(n):
#                 if a[j] not in map_counter and s[j] not in map_counter2:
#                     map_counter[a[j]] = s[j]
#                     map_counter2[s[j]] = a[j]
#                 else:
#                     add1 = s[j] in map_counter2
#                     add2 = a[j]  in map_counter
#                     if s[j] in map_counter2:
#                         if map_counter2[s[j]] != a[j]:
#                             found = False
#                             break
#                     if a[j] in map_counter:
#                         if map_counter[a[j]] != s[j]:
#                             found = False
#                             break
#         if found:
#             print("YES")
#         else:
#             print("NO")

# 1907B
# t = int(input())
# for _ in range(t):
#     s = list(input())
#     n = len(s)
#     upper = []
#     lower = []
#     for i in range(n):
#         if s[i] == "b":
#             s[i] = ''
#             if lower:
#                 s[lower.pop()] = ''
#             continue
#         if s[i] == "B":
#             s[i] = ''
#             if upper:
#                 s[upper.pop()] = ''
#             continue
#         if "a" <= s[i] <= "z":
#             lower.append(i)
#         else:
#             upper.append(i)
#     print("".join(s))


# 1996A
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     if n <= 4:
#         print(1)
#     elif n % 4 == 0:
#         print(n//4)
#     else:
#         print((n//4) + 1)

# 1915C
# from math import sqrt
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     sum_arr = sum(arr)
#     sqrt_arr = int(sqrt(sum_arr))
#     if sqrt_arr * sqrt_arr == sum_arr:
#         print("YES")
#     else:
#         print("NO")


# 2114A
# print(int("0108"))

# import math
# for _ in range(int(input())):
#     s = input()
#     sqrt_s = int(math.sqrt(int(s)))
#     int_s = int(s)
#     if int_s == 0:
#         print(0, 0)
#     elif sqrt_s * sqrt_s != int_s:
#         print(-1)
#     else:
#         print(1, sqrt_s - 1)


# 1744C
# def binary_search_right(arr, target):
#     """Найти крайнюю правую позицию для вставки target в отсортированный массив arr"""
#     left = 0
#     right = len(arr)
#
#     while left < right:
#         mid = (left + right) // 2
#         if target < arr[mid]:
#             right = mid
#         else:
#             left = mid + 1
#
#     return left
#
#
# def solve(n, c, s):
#     if c == 'g':
#         return 0  # Уже зеленый - можно переходить
#
#     # Собираем все позиции зеленых светофоров
#     green_positions = [i for i in range(n) if s[i] == 'g']
#
#     # Расширяем позиции для учета цикличности (добавляем второй цикл)
#     extended_positions = green_positions + [pos + n for pos in green_positions]
#
#     max_wait = 0
#     # Проверяем каждую позицию текущего цвета
#     for i in range(n):
#         if s[i] == c:
#             # Находим индекс первого зеленого света ПОСЛЕ позиции i
#             next_green_idx = binary_search_right(extended_positions, i)
#             wait_time = extended_positions[next_green_idx] - i
#             max_wait = max(max_wait, wait_time)
#
#     return max_wait
#
#
# # Обработка ввода
# t = int(input())
# for _ in range(t):
#     n, c = input().split()
#     n = int(n)
#     s = input()
#     print(solve(n, c, s))

# def bns(arr, target):
#     l = 0
#     r = len(arr)
#     while l < r:
#         mid = (l + r) // 2
#         if target <= arr[mid]:
#             r = mid
#         else:
#             l = mid + 1
#     return l

# n, s = map(int, input().split())
# dorms_orig = list(map(int, input().split()))
# dorms = []
# acc = 0
# for i in dorms_orig:
#     acc += i
#     dorms.append(acc)
# letters = list(map(int, input().split()))
# for j in range(s):
#     appartment_idx = bns(dorms, letters[j])
#     num_appartment = dorms[appartment_idx] - letters[j]
#     num_appartment = dorms_orig[appartment_idx] - num_appartment
#     print(appartment_idx + 1, num_appartment)

