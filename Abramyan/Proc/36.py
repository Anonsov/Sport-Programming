import random
def Fib(N):
    f1 = 1
    f2 = 1
    if N <= 2:
        return 1
    while N > 2:
        f1, f2 = f2, f1 + f2
        N -= 1
    return f2

 
									