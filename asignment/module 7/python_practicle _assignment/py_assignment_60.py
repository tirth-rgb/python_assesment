# Sample string
text = "w3resource"

# Dictionary to store character counts
char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

# Display output
print(char_count)
