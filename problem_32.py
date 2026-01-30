numbers = [45, 12, 78, 34, 89]
minimum = numbers[0]

for num in numbers[1:]:
    if num < minimum:
        minimum = num

print(f"Minimum: {minimum}")

