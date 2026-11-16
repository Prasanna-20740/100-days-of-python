word = input("Enter a word: ").lower().strip()
reversed_word = word[::-1]

if word == reversed_word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
