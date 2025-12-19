# Program to find the sum of three integers
# If any two values are equal, the sum is zero

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

if a == b or b == c or a == c:
    print("Sum is 0")
else:
    print("Sum is:", a + b + c)
