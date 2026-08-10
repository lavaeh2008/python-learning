# Reverse a Word Using a Loop

word = input("Enter a word: ")

for i in range(len(word) - 1, -1, -1):
    print(word[i])