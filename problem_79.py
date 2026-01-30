# Problem 79: Calculate compound interest
# Find and fix the error

def compound_interest(principal, rate, time, n):
    """
    Calculate compound interest.
    principal : initial amount
    rate      : annual interest rate in %
    time      : time in years
    n         : number of times interest applied per year
    """
    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    return amount - principal  # compound interest

# Example usage
p = 1000
r = 5
t = 2
n = 4

ci = compound_interest(p, r, t, n)
print(f"Compound Interest: {ci:.2f}")

