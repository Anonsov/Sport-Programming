# a = "basoluteabn"
# found_ab = False
# found_ba_after_ab = False
# start = 0
# c = ""
# for i in range(len(a) - 1):
#     if a[i:i+2] == "ab":
#         found_ab = True
#         c += a[0:i] + a[i+2:]
#         break
# print(c)
# if "ba" in c:
#     found_ba_after_ab = True

# if found_ab == True and found_ba_after_ab ==True:
#     print("YES")
# else:
#     print("NO")

a = "cabac"
found_ab = False
found_ba = False

for i in range(len(a) - 1):
    if not found_ab and a[i:i+2] == "ab":
        found_ab = True
        i += 1  # Пропускаем следующий символ, чтобы избежать пересечения
    elif not found_ba and a[i:i+2] == "ba":
        found_ba = True
        i += 1  # Пропускаем следующий символ, чтобы избежать пересечения

if found_ab and found_ba:
    print("YES")
else:
    print("NO")