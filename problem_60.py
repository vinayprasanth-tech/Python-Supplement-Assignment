# Problem 60: Check if number is Armstrong number
# Find and fix the error
def is_armstrong(n):
    total = 0
    num = n
    num_digits = len(str(n))
    while num > 0:
        digit = num % 10
        total += digit ** num_digits
        num //= 10
    return total == n

