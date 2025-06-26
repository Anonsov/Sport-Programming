a = [1,2,4,4,3,4,4,5,5,5,5,6,6,6]
count = 0
deleted = False
i = 1
while i < len(a):
    if a[i] == a[i-1]:
        count+=1
    else: 
        count = 0
        deleted = False
    if count >= 1 and deleted == False:
        a.pop(i)
        deleted = True
        i-=1
    i+=1
print(a)