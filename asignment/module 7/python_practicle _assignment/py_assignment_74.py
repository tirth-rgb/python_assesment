# Number of lines to read
n = 5

# Open the file in read mode
with open("example.txt", "r") as file:
    # Read first n lines
    for i in range(n):
        line = file.readline()
        if not line:
            break  # Stop if end of file is reached
        print(line, end="")
