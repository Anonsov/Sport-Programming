a = 2
b = 4
n = 10

length = b-a
for i in range(0, n+1):
    result = 0
    result += a+(i*(length/n))
    print(result)