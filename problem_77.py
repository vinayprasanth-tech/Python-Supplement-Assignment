# Problem 77: Check if number is perfect square
# Find and fix the error
def is_perfect_square(n):
    if n < 0:
        return False  # negative numbers cannot be perfect squares
    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n

# Example usage
print(f"Is 16 perfect square? {is_perfect_square(16)}")  # True
print(f"Is 15 perfect square? {is_perfect_square(15)}")  # False
