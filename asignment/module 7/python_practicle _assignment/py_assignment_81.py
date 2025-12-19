# Sample list
my_list = ["Python", "Java", "C++", "JavaScript"]

# Open the file in write mode
with open("example.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")  # Write each item on a new line

print("List has been written to the file.")
