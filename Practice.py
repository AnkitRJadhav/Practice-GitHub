str1 = "fg hjg kih utb"
lst1 = []
lst2 = []
for i in range(len(str1)):
    if str1[i] == " ":
        lst1.append(i)
    else:
        lst2.append(str1[i])
lst2 = lst2[::-1]
for i in lst1:
    lst2.insert(i, " ")
print("".join(lst2))

