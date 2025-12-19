# Program to count occurrences of a substring without using count()

string = input("Enter the main string: ")
substring = input("Enter the substring: ")

count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        count += 1

print("Number of occurrences:", count)
