word = input("Enter string: ").lower()
vowels = 0
consonants = 0
for letter in word:
    if letter in "aeiou":
        vowels += 1
    elif letter.isalpha():
        consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
