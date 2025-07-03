from random import randint
m = 6
n = 5
matrix = []
x = 0
for i in range(m):
    row = []
    for j in range(m):
        x+=1
        row.append(randint(1, 9))
    matrix.append(row)

for i in matrix:
    print(*i)
    
print()

# for d in range(2*m - 1):
#     if d < m:
#         i = 0
#         j = m - d - 1
#     else:
#         i = d - (m - 1)
#         j = 0
    
#     while i < m and j < m:
#         print(matrix[i][j])
#         i += 1
#         j += 1
#     print("---")
        
# k = m
# for d in range(m - 1):
#     i = 0
#     j = d + 1
#     while i < m and j < m:
#         print(matrix[i][j])
#         i += 1
#         j += 1
#     print("----")    

# for d in range(m - 1):
#     i = 0
#     j = m - d - 1
#     while i < m and j < m:
#         print(matrix[i][j])
#         i += 1
#         j += 1
#     print("----")

# for d in range(m - 1):
#     i = d + 1
#     j = 0
#     while i < m and j < m:
#         print(matrix[i][j])
#         i += 1
#         j += 1
#     print("---")
    
# for d in range(m - 1):
#     i = m - d - 1
#     j = 0
#     while i < m and j < m:
#         print(matrix[i][j])
#         i += 1
#         j += 1
#     print("---")
    
    
    
# побочная диагональ

# for d in range(m - 1):
#     i = d 
#     j = 0
#     while i >= 0 and j < m - 1:
#         print(matrix[i][j])
#         # print(i,j)
#         i -= 1
#         j += 1
#     print('---')
    
# for d in range(m - 1):
#     i = 0
#     j = d
#     while i < m - 1 and j >= 0:
#         print(matrix[i][j])
#         i += 1
#         j -= 1
#     print("---")


# for d in range(m):
#     i = d + 1
#     j = m - 1
#     while i < m and j > 0:
#         print(matrix[i][j])
#         i += 1
#         j -= 1
#     print("---")


# for d in range(m - 1):
#     i = m - d - 1
#     j = m - 1
#     while i < m and j > 0:
#         print(matrix[i][j])
#         i += 1
#         j -= 1
#     print("---")

# k = m
# for i in range(m//2):
#     l = i + 1
#     r = m - i
#     for j in range(l, r-1):
#         matrix[i][j] = 0
        
# for i in matrix:
#     print(*i)



# вывод сверху побочной линии
# j = m - i - 1 and i = iterator from 1 to m -> побочная линия
# j = m - i - 2 and i = iterator from 1 to m  -> линия сверху побочной линии и т.д
# j = m - i - 3 and i = iterator from 1 to m 
# j = m - i - 4 and i = iterator from 1 to m 
# j = m - i - 5 and i = iterator from 1 to m 


# вывод нижней части побочной линии
# i = i + 1
# i = i + 2
# i = i + m - 1