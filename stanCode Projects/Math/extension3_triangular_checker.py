"""
File: extension3_triangular_checker.py
Name: Zoe
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    Ask user to enter a n(integer)
    If the n equals EXIT number, print " Have a good one! "
    Otherwise, if there is one number(i) satisfies the formula i * (i + 1)) / 2 = n,
    n is a triangular number, print " (n) is a triangular number "
    If there is no number(i) satisfies the formula i * (i + 1)) / 2 = n,
    n is a not triangular number, print " (n) is not a triangular number "
    """
    print('Welcome to the triangular number checker!')
    n = int(input('n: '))
    while n != EXIT:
        if is_triangular(n):                                # check whether n is a triangular number
            print(str(n) + ' is a triangular number')       # when the formula is satisfied
        else:
            print(str(n) + ' is not a triangular number')   # when the formula is NOT satisfied
        n = int(input('n: '))
    print('Have a good one!')


def is_triangular(n):                   # check whether n is a triangular number
    """
    :param n: int, the number user entered
    """
    for i in range(1, n):
        if (i * (i + 1)) / 2 == n:      # if i satisfies this formula, n is a triangular number
            return True


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
