# Problem 63: Find longest word in a sentence
# Find and fix the error
def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)
