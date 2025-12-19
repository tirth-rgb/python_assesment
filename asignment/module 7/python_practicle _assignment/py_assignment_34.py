def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Example usage
print(has_common_member([1, 2, 3], [4, 5, 6]))  # False
