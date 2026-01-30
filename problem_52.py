# Problem 52: Find missing number in sequence
# Find and fix the error

def find_missing(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2   # FIXED
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

