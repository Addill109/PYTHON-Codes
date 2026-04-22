sentence = input("Enter a string: ")
new_string = ""
for ch in sentence:
    if ch != " ":
        new_string += ch
print("String without spaces:", new_string)
