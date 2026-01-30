# Problem 47: Check if string starts with a specific character
# Find and fix the error

def starts_with(text, char):
    if not text:        # checks for empty string
        return False
    if text[0] == char:
        return True
    return False
