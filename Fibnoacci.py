terms = int(input("How many terms: "))
x, y = 0, 1
count = 0
while count < terms:
    print(x, end=" ")
    z = x + y
    x = y
    y = z
    count += 1
