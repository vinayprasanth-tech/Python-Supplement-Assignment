# Problem 67: Remove nth element from list
# Find and fix the error

def remove_nth(lst, n):
    # Check if index is valid
    if 0 <= n < len(lst):
        return lst[:n] + lst[n+1:]  # return a new list without nth element
    else:
        return lst  # if index out of bounds, return original list

# Example usage
numbers = [1, 2, 3, 4, 5]
result = remove_nth(numbers, 2)
print(f"After removing: {result}")
