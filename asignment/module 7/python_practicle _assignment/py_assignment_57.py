from collections import Counter

# Two lists
keys = ['a', 'b', 'd', 'c']
values = [400, 400, 400, 300]

# Map lists into a dictionary
my_dict = dict(zip(keys, values))

# Convert to Counter (optional)
counter_dict = Counter(my_dict)

print(counter_dict)
