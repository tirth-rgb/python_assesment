# Open the file in read mode
with open("example.txt", "r") as file:
    # Read all lines into a single string
    content = ""
    for line in file:
        content += line  # Append each line to the variable

# Display the content
print(content)
