# Function That Returns a Value

def count_letters(word):
    return len(word)


user_word = input("Enter a word: ")

print("There are", count_letters(user_word), "letters.")