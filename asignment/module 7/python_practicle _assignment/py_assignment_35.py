# Program to generate squares of numbers from 1 to 30

squares = []

for i in range(1, 31):
    squares.append(i ** 2)

# Print first 5 and last 5 elements
print("First 5 elements:", squares[:5])
print("Last 5 elements:", squares[-5:])
