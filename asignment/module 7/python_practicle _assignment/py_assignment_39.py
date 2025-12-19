# Program to find the second smallest number in a list

numbers = [10, 20, 4, 45, 99, 4]

# Remove duplicates and sort the list
unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) < 2:
    print("There is no second smallest number.")
else:
    print("The second smallest number is:", unique_numbers[1])
