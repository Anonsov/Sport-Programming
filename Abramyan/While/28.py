a1 = 2 
a2 = 0  
e = 1/10**14
k = 1   

while abs(a1 - a2) >= e:  
    a2 = 2 + 1 / a1       
    a1, a2 = a2, 2 + 1 / a2 
    k += 1
    print(a1, a2)

print(f"K = {k}, AK-1 = {a1}, AK = {a2}")