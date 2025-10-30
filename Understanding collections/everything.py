# # deque
# from collections import deque
# a = deque()
# a.append(1)
# a.append(12)
# a.append(14)
# a.popleft()
# print(a)

# print(len(a))


# a = "jasonay"

# l = len(a) // 2
# print(a[l - 1:l+2])

# a ="Ault"
# b = "kelly"
# l = len(a) // 2
# print(a[:l] + b + a[l:])

# s1 = "america"
# s2 = "japan"

# res = s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1]
# print(res)


# str1 = "PyNaTive"

# lower = ""
# upper = ""
# for i in str1:
#     if 97 <= ord(i) <= 122:
#         lower += i
#     elif 65 <= ord(i) <= 90:
#         upper += i
        
# print(lower + upper)
# print(ord("a")) # 97
# print(ord("z")) # 122
# print(ord("A")) # 65
# print(ord("Z")) # 90


# str1 = "P@#yn26at^&i5ve"
# chars = 0
# digits = 0
# symbol = 0
# for i in str1:
#     if 97 <=ord(i) <= 122 or 65 <= ord(i) <= 90:
#         chars += 1
#     elif i.isdigit():
#         digits += 1
#     else:
#         symbol += 1

# print(chars, digits, symbol)



# s1 = "Abc"
# s2 = "Xyzzz"

# s3 = ""
# len1 = len(s1)
# len2 = len(s2)
# min_len = min(len1, len2)

# for i in range(min_len):
#     s3 += s1[i] + s2[-(i+1)]

# if len1 > min_len:
#     s3 += s1[min_len:]
# if len2 > min_len:
#     s3 += s2[:len2 - min_len]
# print(s2[:len2 - min_len])
# print(s3)


# s1 =  "Ynf"
# s2 = "nfY"
# mp = {}

# for i in s1:
#     if i not in mp:
#         mp[i] = 1
# found = True
# for i in s2:
#     if i not in mp:
#         found = False
#         break

# print(found)


# def maxArea(height: list[int]) -> int:
#     i = 0
#     j = len(height) - 1
#     res = 0
    
#     while i < j:
#         res = max(res, (j-i) * min(height[i], height[j]))

#         if height[i] < height[j]:
#             i += 1
#         else:
#             j -= 1

#     return res

# print(maxArea([1,8,6,2,5,4,8,3,7]))


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
        
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
        
#     def add_elem(self, value: int):
#         new_head = Node(value)
#         if self.head == None and self.tail == None:
#             self.head = self.tail = new_head
#         else:
#             self.tail.next = new_head
#             self.tail = new_head
#         self.length += 1
    
#     def add_first(self, value):
#         new_elem = Node(value)
#         new_elem.next = self.head
#         self.head = new_elem
#         self.length += 1
        
        
#     def size(self):
#         print(self.length)
#         return self.length
        
        
#     def __str__(self):
#         res = []
#         curr = self.head
#         while curr != None:
#             res.append(curr.value)
#             curr = curr.next
#             # print(hex(id(curr)))
#         print(*res)
        
#     def print_first(self):
#         print(self.head.value)
#         return self.head.value

#     def print_n(self, n):
#         i = 1
#         curr = self.head
#         while i <= n:
#             curr = curr.next
#             i += 1
#         print(curr.value)
    
#     def insert_n(self, n, ind):
#         new_elem = Node(n)
#         i = 1
#         curr = self.head
#         while i < ind:
#             curr = curr.next
#             i+= 1
            
#         # print("insert", curr.value)
#         new_elem.next = curr.next
#         curr.next = new_elem
#         self.length += 1
    
    
#     def delete_first(self):
#         head = self.head
#         self.head = self.head.next
#         self.length -= 1
#         # head.next = None
#         del head
        
#     def delete_last(self):
#         curr = self.head
#         while curr.next.next != None:
#             curr = curr.next 
#         self.tail = curr
#         self.tail.next = None
#         self.length -= 1
        
#     def delete_n(self, ind):
#         i = 1
#         curr = self.head
#         while i < ind - 1:
#             curr = curr.next 
#             i += 1 
#         curr.next = curr.next.next
#         self.length -= 1
    
#     def remove_elem(self, elem):
#         curr = self.head
#         prev = self.head
       
#         while curr != None:
#             if curr.value == elem:
#                 if curr == self.head:
#                     self.delete_first()
#                 break
#             prev = curr
#             curr = curr.next
        
#         # print(prev.value, curr.value)
        
#         prev.next = curr.next
            
        
        
# ll = LinkedList()
# ll.add_elem(10)
# ll.add_elem(20)
# ll.add_elem(30)
# ll.add_elem(40)
# ll.add_elem(5)
# ll.add_elem(520)
# ll.add_elem(2000)
# ll.add_first(1000)
# ll.add_first(2007)
# ll.add_elem(2008)
# # ll.print_n(3)
# ll.insert_n(900000, 2)
# ll.insert_n(1002, 3)
# # ll.size()
# ll.delete_first()
# ll.delete_first()
# ll.delete_first()
# ll.delete_last()
# ll.delete_last()
# ll.delete_n(3)
# ll.delete_n(3)
# # ll.remove_elem(40)
# # ll.remove_elem(1002)
# ll.remove_elem(520)
# ll.__str__()
# print(" ")

# # ll.size()
# # print("massive")
# # a = [2007, 1000, 900000, 1002, 10, 20, 30, 40, 5, 520, 2000, 2008]
# # for i in a:
# #     print(hex(id(i)))
# # ll.print_first()

# # a = [1,2,3,4,5]
# # for i in a:
# #     print(hex(id(i)))


# a = [2,4,3]
# b = [5,6,4]

