# Python 3.8

# Problem Statement:
"""
Make a Factorial Calculator that inputs a number (n) and outputs the factorial of the
number (n!)
                Constraint      Example 1       Example 2
Input          0 < x < 10           5               9
Output      1 < y < 3628800        120           362880
"""

# Solution:
""" The function that calculates the factorial of the input integer using recursion """
def factorial_with_recursion(n):
    while 0 < n < 10:
        try:
            if n == 1:
                return n
            else:
                return n * factorial_with_recursion(n - 1)
        except ValueError:
            print("ValueError occurred!")


if __name__ == "__main__":
    x = int(input("Enter a number between 0 and 10 (Excluding 0 and 10): "))
    y = int(factorial_with_recursion(x))
    if 1 < y < 3628800:
        print('\nThe factorial of {} is {}'.format(x, y))
