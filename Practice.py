str1 = "N56K4LM6"
lst1 = []
lst2 = []
for i in str1:
    if str(i).isnumeric():
        lst2.append(i)
    else:
        lst1.append(i)
lst1.sort()
lst2.sort()
for i in range(len(str1)):
    if str1[i].isnumeric():
        lst1.insert(i, lst2[0])
        lst2.__delitem__(0)
str2 = ""
for i in lst1:
    str2 += i
print(str2)
