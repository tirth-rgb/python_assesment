# Function to insert a string in the middle of another string

def insert_string_middle(main_string, insert_string):
    middle = len(main_string) // 2
    result = main_string[:middle] + insert_string + main_string[middle:]
    return result

# Example usage
text = input("Enter the main string: ")
insert = input("Enter the string to insert: ")

print("Result:", insert_string_middle(text, insert))
