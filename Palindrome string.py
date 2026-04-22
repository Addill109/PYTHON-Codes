word = input("Enter a string: ")
rev = ""
for i in word:
    rev = i + rev
if word == rev:
    print(word, "is a Palindrome")
else:
    print(word, "is not a Palindrome")
