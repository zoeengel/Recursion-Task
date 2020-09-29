your_word = input("Enter your word: ")
def is_palindrome(your_word):
    return your_word == your_word[::-1]
print("This is", is_palindrome(your_word))



