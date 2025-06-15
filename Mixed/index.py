# def to_camel_case(text):
#     res = ""
#     for i in range(0, len(text) - 1):
#         if text[i] == "-" or text[i] == "_":
            
#             res += text[i+1].upper()
#         else:
#             i+=1
#             res += text[i]
#     for i in res:
#         if i == "-":
#             res = res.replace("-", '')
#         elif i == "_":
#             res = res.replace("_", '')
#     return text[0] + res



# print(to_camel_case("The-Pippi-Was_kawaii"))

# print(9//10/)

# def narcissistic( n ):
#     numbers = []
#     original = n
#     while n > 0:
#         zero = n % 10
#         numbers.append(zero)
#         n //= 10
    
    


# print(narcissistic(153))


# def order(sentence):
    
    

# print(order("is2 Thi1s T4est 3a"))


# def order(sentence):
#     if not sentence:
#         return ""
    
#     words = sentence.split(" ")
#     orders = [""] * len(words)

#     for word in words:
#         for char in word:
#             if char.isdigit():
#                 char = int(char) - 1
#                 orders[char] = word

#     return ' '.join(orders)


# print(order("is2 Thi1s T4est 3a"))


# def tribonacci(signature, n):
#     if n < len(s    ignature):
#         return signature[:n]
#     i = 0
#     while i < n-3:
#         signature.append(sum(signature[i:]))
#         i+=1
#     return signature

# print(tribonacci([3, 2, 1], 3))
# n = 9
# for i in range(n, 0, -1):
#     b = ""
#     for x in range(1, i + 1):
#         b += str(x)
#     print(b)

# def valid_braces(string):
    
#     while "{}" in string or "()" in string or "[]" in string:
#         string = string.replace("[]", "")
#         string = string.replace("{}", "")
#         string = string.replace("()", "")
    
#     return string == ""

# print(valid_braces("[({})](]"))

# def unique_in_order(sequence):
#     if len(sequence) == 0:
#         return []
#     if len(sequence) == 1:
#         return [sequence]

#     res = []
#     for i in range(1, len(sequence)):
#         if sequence[i-1] != sequence[i]:
#             res.append(sequence[i-1])
#     if sequence[-1] != res[-1]:
#         return res + [sequence[-1]]
#     else:
#         return res
# print(unique_in_order(["a", "b", "b", "a"]))

# a = [6,43,65,3,61,7]
# b = 13
# c = {}
# for i in range(len(a)):
#     x = b - a[i]
#     if x in c:
#         print([c[x], i])
#     c[a[i]] = i






# def unique_in_order(sequence):
#     res = []
#     prev = None
    
#     for i in sequence:
#         if i != prev:
#             res.append(i)
#             prev = i
#     return res

# print(unique_in_order(""))



# def is_pangram(st):
    
#     return len(sorted({x for x in st.lower() if x.isalpha()}, reverse=True)) == 26
# print(is_pangram(',FCDzggoil tK2|OalEyq&\x0bTpCatX" BsNGf2MW.JJ2iD?I vIr\x0cjnPhu9kF'))



# def dig_pow(n, p):
#     stringed = str(n)[::-1]
#     n = int(stringed)
#     summedDigits = 0
#     digits = 0
#     while n > 0:
#         digits = n % 10
#         n //= 10
#         summedDigits += digits**(p)
#         p += 1
#     result = summedDigits / int(stringed[::-1])
#     if int(result) == result:
#         return int(result)
#     else:
#         return -1


# print(dig_pow(92, 1))

# def solution(s):
#     # count = 0
#     index = 0
#     res = []
#     while index < len(s):
#         res.append(s[index:index+2])
#         # count += 2
#         index += 2
#     if len(s) % 2 != 0:
#         return res[:-1] + [res[-1] + "_"]
#     else: 
#         return res
    


# print(solution("asdfasfdklkl"))



# def find_uniq(arr):
#     arr = sorted(arr)
#     if arr[0] == arr[1]:
#         return arr[-1]
#     else:
#         return arr[0]

# print(find_uniq([1,1,1,1,5,1,1]))


# def sort_array(source_array):
#     odds = []
#     odds_index = []
#     for i in range(0, len(source_array)):
#         if source_array[i] % 2 != 0:
#             odds_index.append(i)
#             odds.append(source_array[i])
#     odds = sorted(odds)
#     for i in range(0, len(odds)):
#         source_array[odds_index[i]] = odds[i]   
          
#     return source_array

# print(sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]))



# a = ['a','b','c','d','f']
# for i in a:
#     print(ord(i))
# hashmap = {}
# def find_missing_letter(chars):
#     ords = []
#     for i in range(0, len(chars)):
#         ords.append(ord((chars[i])))
#         # print(ords)
#     for i in range(0, len(ords) - 1):
#         if int(ords[i]) - int(ords[i+1]) == -2:
#             return chr(ords[i] + 1)
# print(find_missing_letter(['O','Q','R','S']))







# def tower_builder(n_floors):
#     res = []
#     zvezda = 1
#     spaces = n_floors
#     i = 0
#     while i < n_floors:
# #         zvezda += 2
#         spaces -= 1
#         res.append(spaces * " " + zvezda*"*" + spaces* " ")
#         i+= 1
#         zvezda += 2
#     return res

# print(tower_builder(3))


# def high(x):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     hashmap = {}
#     for i in range(0, len(alphabet)):
#         hashmap[alphabet[i]] = i+1
#     max = 0
#     count = 0
#     for i in range(0, len(x)):
#         if x[i] != " ":
#             count += hashmap[x[i]]
#         else:
#             if max < count:
#                 max = count
#                 print(max)



# print(high("aa b ccc"))


# def high(x):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     hashmap = {alphabet[i]: i + 1 for i in range(len(alphabet))}
#     words = x.split(" ")
#     result = ""
#     max = 0
#     for i in words:
#         score = 0
#         for j in i:
#             score += hashmap[j]
#         if max < score:
#             result = i
#             max = score
#     return result

# print(high("man ixxxxx need a taxi up to xxxx ubud"))





# def delete_nth(order,max_e):
#     res = []
#     hashmap = {}
#     for i in order:
#         if i in hashmap:
#             hashmap[i] += 1
#             if hashmap[i] > max_e:
#                 hashmap[i] = max_e
#         else:
#             hashmap[i] = 1
    
    
# print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))



# def delete_nth(order, max_e):
#     counter = {}
#     res = []
#     for i in order:
#         if i in counter:
#             counter[i] += 1
#         else:
#             counter[i] = 1
        
#         if counter[i] <= max_e:
#             res.append(i)
#     return res


# print(delete_nth([20, 37, 20, 21], 1))


# def solution(s):
#     res = ""
#     for i in s:
#         if ord(i) < 96:
#             res += " "
#         res+= i
#     return res
# print(solution("helloWorld"))

# c = "hello"

# if "ll" in c:

# def next_states(s):
#     result = []
#     if s[-1] =="I": result.append(s + "U")
#     if s[0] == "M": result.append(s[0] + (s[1:]) * 2)
    
#     for i in range(len(s)):
#         if s[1:i]


# print(next_states("MI"))




# def next_states(s):
#     res = []
#     if s[-1] == "I": res.append(s + "U")
#     if s[0] == "M": res.append(s[0] + (s[1:] * 2))

#     for i in range(0, len(s)):
#         if s[i:i+3] == "III":
#             res.append(s[:i] + "U" + s[i+3:])
    
#     for i in range(0, len(s)):
#         if s[i:i+2] == "UU":
#             if res[-1] != s[:i] + s[i+2:]:
#                 res.append(s[:i] + s[i+2:])

#     return res

# if next_states("MIIIIIIIIU") == ['MIIIIIIIIUIIIIIIIIU', 'MUIIIIIU', 'MIUIIIIU', 'MIIUIIIU', 'MIIIUIIU', 'MIIIIUIU', 'MIIIIIUU']:
#     print(True)
# print(next_states("MUUUI"))
# def make_readable(seconds):
#     if seconds < 60:
#         return f"00:00:{"0" + str(seconds)  if seconds < 10 else seconds}"
#     elif seconds < 3600:
#         return f"00:{"0" + str(seconds//60) if seconds//60 < 10 else seconds // 60}:{"0" + str(seconds%60) if seconds%60 < 10 else seconds%60}"
#     elif seconds < 360000:
#         return f"{"0" + str(seconds//3600) if seconds//3600 < 10 else seconds//3600}:{("0" + str(seconds%3600)//60)}:{seconds%60}"
    
        


# print(make_readable(3699))




# def dir_reduc(arr):
    # hashmap = {}
    # for i in arr:
    #     if i not in hashmap:
    #         hashmap[i] = 1
    #     else: 
    #         hashmap[i] += 1
    # # ns = 0
    # if hashmap["NORTH"] and hashmap["SOUTH"]:
    #     if hashmap["NORTH"] > hashmap["SOUTH"] or hashmap["NORTH"] == hashmap["SOUTH"]:
    #         hashmap["NORTH"] = hashmap["NORTH"] - hashmap["SOUTH"]
    #         hashmap["SOUTH"] = 0
    #     elif hashmap["NORTH"] < hashmap["SOUTH"]:
    #         hashmap["SOUTH"] =  hashmap["SOUTH"] - hashmap["NORTH"]
    #         hashmap["NORTH"] = 0
    # if hashmap["EAST"] and hashmap["WEST"]:
    #     if hashmap["EAST"] > hashmap["WEST"] or hashmap["EAST"] == hashmap["WEST"]:
    #         hashmap["EAST"] = hashmap["EAST"] - hashmap["WEST"]
    #         hashmap["WEST"] = 0
    #     elif hashmap["EAST"] < hashmap["WEST"]:
    #         hashmap["WEST"] = hashmap["WEST"] - hashmap["EAST"]
    #         hashmap["EAST"] = 0
    # res = []
    # for i in arr:
    #     if hashmap[i]:
    #         if hashmap[i] > 0:
    #             res.append(i)
    #             hashmap[i] -= 1
            


    # return res




# print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "NORTH"]))

# opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

# def dirReduc(plan):
#     new_plan = []
#     for d in plan:
#         if new_plan and new_plan[-1] == opposite[d]:
#             new_plan.pop()
#         else:
#             new_plan.append(d)
#     return new_plan

# print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "NORTH"]))


# // Вход: Массив чисел
# // Выход: Строка с диапазонами
# // Необходимо преобразовать полученный на вход массив в строку
# // сворачивая соседние по числовому ряду числа в диапазоны

# range([1, 4, 5, 2, 3, 9, 8, 11, 0]); // '0-5,8-9,11'
# range([1, 4, 3, 2]); // '1-4'

# function range(arr) {}

# res = ""
# def func(arr):
#     global res
#     arr = sorted(arr)
#     for i in range(0, len(arr) - 1):   
#         res += str(arr[0])     
#         if arr[i+1] - arr[i] != 1:
#             res += str(arr[i])
#     return func(arr[i:])

# print(func([1, 4, 5, 2, 3, 9, 8, 11, 0]))

# def rot13(message):
#     res = ""
#     for i in message:
#         print(ord(i.lower()))
#         # if ord(i.lower()) + 13 > 123 and:
#         #     res += chr((122 - ord(i.lower())) + 96)

#         # if ord(i.lower()) + 13 > 123  and (96 < ord(i.lower()) < 123):
#         #     res += chr((122 - ord(i.lower())) + 97)
#         #     print(chr(122 - ord(i.lower()) + 97), 122 - ord(i.lower()) + 97)
#         # if ord(i.lower()) + 13 < 123 and (96 < ord(i.lower()) < 123):
#         #     res += chr(13 + ord(i))
#         #     print(chr(13 + ord(i)), ord(i) + 13)x
            
#     return res

# print(rot13("test"))

# def generate_hashtag(s):
#     print(len(s))
#     res = "#"
#     counter_cap = 0
#     for i in s:
#         if i != " ":
#             if counter_cap == 0:
#                 res += i.upper()
#             else: 
#                 res += i.lower()
#             counter_cap += 1
#         else:
#             counter_cap = 0
            
#     if len(res) > 140 or res == "#":
#         return False
#     return res


# print(generate_hashtag("ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq"))


# def find_even_index(arr):
#     left = 1
#     right = len(arr) - 1
#     # index = 0
#     count = 0
#     while left < right:
#         if sum(arr[:left]) == sum(arr[right:]):
#             count += 1
#             left += 1
#             right -= 1
#         else:
#             return -1
#     return count

# print(find_even_index([10, -10]))



