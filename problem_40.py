# Problem 40: Count consonants in a string
# Find and fix the error
def count_consonants(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.isalpha() and char.lower() not in vowels:
            count += 1
    return count

