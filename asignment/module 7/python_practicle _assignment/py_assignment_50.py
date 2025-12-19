# Sample dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'Paris'}

# Key to check
key_to_check = 'age'

# Method 1: Using 'in' keyword
if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does NOT exist in the dictionary.")

# Method 2: Using get() method
if my_dict.get(key_to_check) is not None:
    print(f"Key '{key_to_check}' exists (checked using get()).")
else:
    print(f"Key '{key_to_check}' does NOT exist (checked using get()).")
