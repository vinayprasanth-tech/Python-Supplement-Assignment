# Problem 51: Reverse words in a sentence
# Find and fix the error

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()          # FIX: reverse word order
    return " ".join(words)


text = "Hello World"
print(f"Reversed words: {reverse_words(text)}")
