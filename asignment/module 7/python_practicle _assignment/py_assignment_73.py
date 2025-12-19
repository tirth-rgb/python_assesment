# Text to append
text_to_append = "This is the new text to add.\n"

# Open file in append mode and write text
with open("example.txt", "a") as file:
    file.write(text_to_append)

# Open the file in read mode to display content
with open("example.txt", "r") as file:
    content = file.read()

print("File content after appending:")
print(content)
