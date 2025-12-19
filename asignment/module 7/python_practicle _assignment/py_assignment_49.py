# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Method 1: Using dictionary unpacking (Python 3.5+)
new_dict = {**dict1, **dict2, **dict3}
print("Concatenated dictionary:", new_dict)

# Method 2: Using update()
new_dict2 = dict1.copy()  # Make a copy to avoid changing dict1
new_dict2.update(dict2)
new_dict2.update(dict3)
print("Concatenated dictionary (using update):", new_dict2)
