# x = 3
# n = 4
# result = 0
# sign = 1

# for i in range(1, 2*n, 2):
#     v1 = 1
#     v2 = 1
#     for j in range(1, i, 2):
#         v1 *= j
#     for k in range(2, i+1, 2):
#         v2 *= k
    
#     result += sign * (v1*(x**(i-1)))/v2*((i-1)*2)
#     sign *= -1
# print(result)

s = input()
a = ['(', '{', '[']
b = [')', '}', ']']
x = []

for i in s:
    if i in a:
        x.append(i)
    elif i in b:
        if not x or b.index(i) != a.index(x.pop()):
            print("NO")
            break
if not x:
    print("YES")

