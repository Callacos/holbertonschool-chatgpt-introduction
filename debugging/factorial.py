#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Usage: ./script.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

f = factorial(n)
print(f"Factorial of {n} is {f}")
