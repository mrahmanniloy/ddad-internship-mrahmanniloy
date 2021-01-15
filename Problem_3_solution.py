# Python 3.8

# Problem Statement:
"""
Write a program that displays whether a given string is either an Even Palindrome, an
Odd Palindrome or Not a Palindrome. Solving it using recursion will land you bonus 5
points
            Example 1           Example 2               Example 3
Input       Ababa               sfe3443efs              ssee2344s
Output   Odd Palindrome     Even Palindrome         Not a Palindrome
"""

# Solution:
""" The recursive function to check palindrome """
def palindrome_checker(string):
    return string == string[::-1]


if __name__ == '__main__':
    input_string = str(input("Enter a string: "))
    if palindrome_checker(input_string):
        if len(input_string) % 2 == 0:
            print("\nEven Palindrome")
        else:
            print("\nOdd Palindrome")
    else:
        print("\nNot a Palindrome")
