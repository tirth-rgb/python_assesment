# Number of lines to read from the end
n = 5

# Open the file in read mode
with open("example.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list

# Get the last n lines
last_lines = lines[-n:]

# Display the last n lines
for line in last_lines:
    print(line, end="")
