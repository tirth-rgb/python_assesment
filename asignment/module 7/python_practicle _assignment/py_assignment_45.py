# Original list of tuples
tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzipping using zip(*)
list1, list2 = zip(*tuple_list)

# Convert tuples to lists
list1 = list(list1)
list2 = list(list2)

print("First list:", list1)
print("Second list:", list2)
