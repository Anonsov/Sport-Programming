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
            
