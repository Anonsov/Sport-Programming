n = [1,1,2,5,9,5,2,6]
k = 3
l = 6
sum = 0
for i in range(0, l + 1):
    if i >= k and i <= l + 1:
       sum += n[i] 
print(sum/((l-k) + 1), n[k-1:l])