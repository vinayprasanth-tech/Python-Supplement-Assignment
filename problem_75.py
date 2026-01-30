# Problem 75: Check if parentheses are balanced
# Find and fix the error

def are_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

# Example usage
expr = "((a + b) * (c - d))"
print(f"Balanced: {are_balanced(expr)}")

