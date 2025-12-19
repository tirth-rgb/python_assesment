# Sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merge dict2 into dict1
merged_dict = dict1.copy()  # Make a copy to avoid changing dict1
merged_dict.update(dict2)

print("Merged dictionary:", merged_dict)
