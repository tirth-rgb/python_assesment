# Program to get a string made of first 2 and last 2 characters

text = input("Enter a string: ")

if len(text) < 2:
    result = ""
else:
    result = text[:2] + text[-2:]

print("Result:", result)
