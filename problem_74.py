# Problem 74: Find first non-repeating character
# Find and fix the error

def first_non_repeating(text):
    char_count = {}
    
    # Count frequency of each character
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find first character with frequency 1
    for char in text:
        if char_count[char] == 1:
            return char
    
    return None  # if no non-repeating character exists

# Example usage
word = "programming"
print(f"First non-repeating: {first_non_repeating(word)}")
