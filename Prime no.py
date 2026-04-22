num = int(input("Enter a number: "))
flag = True
if num < 2:
    flag = False
for i in range(2, num):
    if num % i == 0:
        flag = False
        break
if flag:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")
