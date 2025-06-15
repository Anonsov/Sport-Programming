first = 1000
p = 25
months = 0
while first <= 1100:
    first+=int(first*p)/100
    months+=1
print(months)