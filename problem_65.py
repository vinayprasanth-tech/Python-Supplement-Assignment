# Problem 65: Check if list has duplicates
# Find and fix the error

def has_duplicates(lst):
    seen = set()  # use a set for faster lookup
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

# Example usage
numbers = [1, 2, 3, 4, 5]
print(f"Has duplicates: {has_duplicates(numbers)}")  # Output: False

numbers_with_dupes = [1, 2, 3, 2, 5]
print(f"Has duplicates: {has_duplicates(numbers_with_dupes)}")  # Output: True

