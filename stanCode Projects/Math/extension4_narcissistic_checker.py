"""
File: extension4_narcissistic_checker.py
Name: Zoe
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    Ask user to enter a n(integer)
    If the n equals EXIT number, print " Have a good one! "
    If the sum of digits each raised to the power of the number of digits,
    n is a narcissistic number, print " (n) is a narcissistic number "
    Otherwise, n is a not narcissistic number, print " (n) is not a narcissistic number "
    """
    print('Welcome to the narcissistic number checker!')
    n = int(input('n: '))
    while n != EXIT:
        if is_narcissistic(n):                                  # check whether n is a narcissistic number
            print(str(n) + ' is a narcissistic number')         # when the formula is satisfied
        else:
            print(str(n) + ' is not a narcissistic number')     # when the formula is NOT satisfied
        n = int(input('n: '))
    print('Have a good one!')


def is_narcissistic(n):
    """
    :param n: int, the number user entered
    """
    total = 0                       # record the sum of digits raised to the power of the number of digits
    m = n                           # must assign n to m because n cannot be changed
    while m != 0:
        check_digit = m % 10                            # check the units digits (remainder)
        total = total + check_digit ** len(str(n))      # record the sum
        m = m // 10                                     # delete the units digit (153 -> 15)
    if total == n:                  # if total == n, n is a narcissistic number
        return True


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
