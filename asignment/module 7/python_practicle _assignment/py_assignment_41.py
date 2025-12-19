# Function to check if a list contains a sublist
def contains_sublist(main_list, sub_list):
    sub_len = len(sub_list)
    for i in range(len(main_list) - sub_len + 1):
        if main_list[i:i+sub_len] == sub_list:
            return True
    return False

# Example usage
main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4, 5]

if contains_sublist(main_list, sub_list):
    print("Main list contains the sublist.")
else:
    print("Main list does NOT contain the sublist.")
