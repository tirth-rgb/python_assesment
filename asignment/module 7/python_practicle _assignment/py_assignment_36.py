# Function to return unique elements from a list
def unique_list(original_list):
    unique = []
    for item in original_list:
        if item not in unique:
            unique.append(item)
    return unique

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", my_list)
print("Unique list:", unique_list(my_list))
