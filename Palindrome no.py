number = int(input("Enter a number: "))
original = number
reversed_num = 0
while number > 0:
    r = number % 10
    reversed_num = reversed_num * 10 + r
    number //= 10
if reversed_num == original:
    print(original, "is a Palindrome")
else:
    print(original, "is not a Palindrome")
