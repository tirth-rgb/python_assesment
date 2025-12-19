# Function to get largest, smallest, and sum of numbers in a list

def list_operations(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    return largest, smallest, total

# Example usage
my_list = [10, 5, 20, 8, 15]

largest, smallest, total = list_operations(my_list)

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of all elements:", total)
