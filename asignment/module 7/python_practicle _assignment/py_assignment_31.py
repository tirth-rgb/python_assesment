# Program to count strings with length >= 2
# and same first and last character

strings = input("Enter strings separated by space: ").split()

count = 0
for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Number of valid strings:", count)
