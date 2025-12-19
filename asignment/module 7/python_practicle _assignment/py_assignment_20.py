# Program to swap first two characters of two strings

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Swap first two characters
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

# Combine both strings
result = new_str1 + " " + new_str2

print("Result:", result)
