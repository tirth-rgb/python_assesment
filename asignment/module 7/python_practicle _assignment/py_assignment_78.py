# Sample text
text = "Python is a powerful programming language"

# Split text into words
words = text.split()

# Find the length of the longest word
max_length = max(len(word) for word in words)

# Find all words with the maximum length
longest_words = [word for word in words if len(word) == max_length]

print("Longest word(s):", longest_words)
