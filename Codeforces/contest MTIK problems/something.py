# n = int(input())
# arr = list(map(int, input().split()))
# q = int(input())
# for i in range(0, q):
#     c = list(map(int, input().split()))
#     for i in range(0, len(arr)):
#         if c[0] <= i <= c[1]:
#             arr[i - 1] += c[-1]

# print(arr)     

# n = 4
# a1 = 1
# a2 = 1
# for i in range(0, n-1):
#     a1, a2 = a2, a1+a2
# print(a1)


# a = list(map(int, input().split()))
# res = {}
# for i in a:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1

# for i in res:
#     if res[i] == 2:
#         print(i)

# k = int(input())



# st = list(map(str, input().split(".")))
# flag = True
# print(st)
# for i in st:
#     for j in i:
#         if (ord(j) == 0 or 49 <= ord(j) <= 57) and (len(st) == 4):
#             flag = True
#         else:
#             flag = False
#             break
# if flag:
#     print("YES")
# else:
#     print("NO")


# st = input().split(".")
# # print(st)
# flag = True
# if len(st) == 4:
#     for i in st:
#         if i.isdigit():
#             s = int(i)
#             if (0 <= s <= 255) == False:
#                 flag = False
#                 break
#         else:
#             flag = False
# else:
#     flag = False

# if flag:
#     print("YES")
# else:
#     print("NO")
    
    
# print("0F4".isdigit())

# import math
# n = int(input())
# c = 0
# for i in range(1, int(math.sqrt(n)) + 1):
#     if n%i == 0:
#         c+=2
#         if i*i == n:
#             c-=1
# print(c)
            
            
# a,b,c = map(int, input().split())
# s1 = a//c
# s2 = b//c
# res = s1*s2
# print(res)            

# map_counter = {}
# s = 0
# res = []

# st = input()

# for i in st:
#     if i in map_counter:
#         map_counter[i] +=1
#     else:
#         map_counter[i] = 1
    
#     if map_counter[i] % 2 == 0:
#         s-=1
#     else:
#         s+=1
    
#     if s <= 1:
#         res.append("YES")
#     else:
#         res.append("NO")
        
# print(*res)



from math import sqrt
n = int(input())
res = {}
res = []
for i in range(2, int(sqrt(n))+2):
    res.append()
         



# В магазине есть N (1 ≤ N ≤ 100) мячиков и K (1 ≤ K ≤ 100) видов краски. Мячики лежат в одном ряду. Продавец хочет покрасить все мячики, но при этом условие не должно нарушатся. Условие в том, что никакие 2 соседние мячики не должны иметь одинаковый цвет. Вы должны найти, сколькими вариантами можно это сделать. Если ответ слишком большой, нужно вывести его с остатком от 1000000007.
