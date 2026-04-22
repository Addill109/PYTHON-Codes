user_input = input("Enter a string: ")
total = 0
for i in user_input:
    if i.isdigit():
        total += 1
print("Total digits found:", total)
