# Input string
text = input("Enter a string: ")

# Dictionary to store letter counts
letter_count = {}

# Count each letter
for char in text:
    if char.isalpha():        # consider only letters (optional)
        char = char.lower()   # make it case-insensitive (optional)
        letter_count[char] = letter_count.get(char, 0) + 1

# Display result
print("Letter count dictionary:")
print(letter_count)
