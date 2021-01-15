# Python 3.8

# Problem Statement
"""
Write a program that displays (prints) the first ‘n’ numbers of the Fibonacci sequence of
the input (n)

            Constraint         Example 1        Example 2
Input(n)    1 < n < 20             4               8
Output                        0, 1, 1, 2     0, 1, 1, 2, 3, 5, 8, 13
"""

# Solution (Faster than recursion)
""" The function that calculates the first 'n' numbers of the Fibonacci sequence of the input 'n' """
def fibNum(n):
    if n <= 1:
        return n
    arr = []
    while len(arr) < n:
        arr.append(0)  #Initiating an empty list(used as an array) with 'n' number of zeros
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i - 2]  #Calculating and replacing the zeros with the numbers of the Fibonacci sequence to the list
    return arr


if __name__ == '__main__':
    input_n = int(input("Enter a number between 1 and 20 (Excluding 1 and 20): "))
    print("\nThe first {} numbers of the Fibonacci sequence of {} are: ".format(input_n, input_n))
    if 1 < input_n < 20:
        y = fibNum(input_n)
        print(', '.join(map(str, y)))
