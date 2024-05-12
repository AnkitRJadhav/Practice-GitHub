str1 = "AaBcDcde"
str2 = ""
for i in str1:
    if str1.lower().count(i.lower()) > 1:
        pass
    else:
        str2 += i
for i in str2:
    for j in range(len(str1)):
        if i == str1[j]:
            print("Index of ", i, " is ", j)

