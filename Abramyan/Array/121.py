a = [1,1,3,3,3,5,5,5,5,5,5,2,2,2,2]
# print(len(a))
k = 5
i = 1
cnt = 1
length = 1
found = False
while i < len(a):
    element = a[i-1]
    if a[i] == a[i-1] and len(a) - 1 != i:
        length+=1
    else:
        if cnt == k:
            found = True
            # print(length, "is the length of the ", a[i], "value")
            while length > 0:
                a.insert(i, element)
                length -= 1
                i+=1
                
        cnt += 1    
        length = 1 
    i+=1    

print(a)