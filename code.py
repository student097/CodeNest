# A simple Python program to calculate the factorial of a number

def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()