string = input("Enter string: ")
d = {}
for i in string:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for key in d:
    print(key, "appears", d[key], "times")
