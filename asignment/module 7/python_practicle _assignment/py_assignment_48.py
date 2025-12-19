# Original dictionary
my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

# Sort dictionary by value (ascending)
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order:", sorted_asc)

# Sort dictionary by value (descending)
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", sorted_desc)
