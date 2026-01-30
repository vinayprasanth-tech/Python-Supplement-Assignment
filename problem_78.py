# Problem 78: Find duplicate elements in list
# Find and fix the error

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)  # add to set to keep unique duplicates
        else:
            seen.add(item)
    return list(duplicates)

# Example usage
numbers = [1, 2, 3, 2, 4, 3, 5]
print(f"Duplicates: {find_duplicates(numbers)}")
