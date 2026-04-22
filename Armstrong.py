num = int(input("Enter number: "))
order = len(str(num))
temp = num
sum = 0
while temp != 0:
    d = temp % 10
    sum += d ** order
    temp //= 10
if sum == num:
    print(num, "is Armstrong")
else:
    print(num, "is not Armstrong")
