# Open the file in read mode
with open("example.txt", "r") as file:
    # Read each line and store in a list
    lines_list = [line.rstrip("\n") for line in file]

# Display the list
print(lines_list)
