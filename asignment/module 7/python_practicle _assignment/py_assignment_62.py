def is_in_range(num, start, end):
    return start <= num <= end

# Example usage
number = 7
lower = 5
upper = 10

if is_in_range(number, lower, upper):
    print(f"{number} is in the range {lower} to {upper}")
else:
    print(f"{number} is not in the range {lower} to {upper}")
