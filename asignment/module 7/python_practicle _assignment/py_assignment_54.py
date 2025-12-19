# Sample dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'Paris'}

# Keys to check
keys_to_check = ['name', 'age', 'country']

# Method 1: Using all() function
if all(key in my_dict for key in keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")

# Method 2: Check individually and report
for key in keys_to_check:
    if key in my_dict:
        print(f"Key '{key}' exists.")
    else:
        print(f"Key '{key}' does NOT exist.")
