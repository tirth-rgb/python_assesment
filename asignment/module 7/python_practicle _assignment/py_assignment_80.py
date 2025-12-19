from collections import Counter

# Open the file in read mode
with open("example.txt", "r") as file:
    # Read the file content
    text = file.read()

# Convert text to lowercase and split into words
words = text.lower().split()

# Count the frequency of each word
word_count = Counter(words)

# Display the word frequencies
for word, count in word_count.items():
    print(f"{word}: {count}")
