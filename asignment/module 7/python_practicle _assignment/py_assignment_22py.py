# Function to reverse a string if its length is a multiple of 4

def reverse_if_multiple_of_4(text):
    if len(text) % 4 == 0:
        return text[::-1]
    else:
        return text

# Example usage
string = input("Enter a string: ")
result = reverse_if_multiple_of_4(string)
print("Result:", result)
