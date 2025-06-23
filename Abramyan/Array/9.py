arr = [3,1,5,14,2,41,51,12]
k = 0
ind = len(arr) - 1
for i in range(0, ind + 1):
    if arr[ind] % 2 == 0:
        print(arr[ind])
        k+=1
    ind-=1
    