first = 10
summarniy = first
p = 10
k = 0
while summarniy < 200:
    first += first*p/100
    summarniy += first
    k+=1
print(k)