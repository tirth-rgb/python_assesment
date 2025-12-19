# Program to modify a string based on given rules

text = input("Enter a string: ")

if len(text) < 3:
    result = text
elif text.endswith("ing"):
    result = text + "ly"
else:
    result = text + "in"

print("Result:", result)
