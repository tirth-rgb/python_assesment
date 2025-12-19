# Program to count character frequency in a string

text = input("Enter a string: ")
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character frequency:")
for ch in frequency:
    print(ch, ":", frequency[ch])
