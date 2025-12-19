# Program to check conditions for two integers

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

if a == b or (a + b) == 5 or abs(a - b) == 5:
    print(True)
else:
    print(False)
