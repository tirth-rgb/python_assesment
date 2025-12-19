# Custom exception for even numbers
class EvenNumberError(Exception):
    pass

try:
    # Take input from user
    num = int(input("Enter an odd number: "))
    
    # Check if number is odd
    if num % 2 == 0:
        raise EvenNumberError(f"{num} is not an odd number!")
    else:
        print(f"Thank you! You entered an odd number: {num}")

except ValueError:
    print("Invalid input! Please enter an integer.")

except EvenNumberError as e:
    print(e)
