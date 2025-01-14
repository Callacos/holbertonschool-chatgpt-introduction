#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number n using recursion.

    Parameters:
    n (int): The number for which the factorial is to be calculated. Must be non-negative.

    Returns:
    int: The factorial of the given number. Returns 1 if n is 0.
    
    Raises:
    ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    """
    Entry point of the program. Reads an integer from the command-line arguments,
    calculates its factorial, and prints the result.
    
    Usage:
    Run the script from the command line with an integer as an argument:
    $ ./script.py <number>
    
    Example:
    $ ./script.py 5
    Output: 120
    """
    if len(sys.argv) != 2:
        print("Usage: ./script.py <number>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        f = factorial(num)
        print(f)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
