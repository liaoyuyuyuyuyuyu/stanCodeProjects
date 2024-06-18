"""
File: extension2_number_checker.py
Name: Zoe
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    Ask user to enter a n(integer)
    If the total of the factor of n equals data, print " (n) is a perfect number "
    If the total of the factor of n is lager than data, print " (n) is a abundant number "
    If the total of the factor of n is less than data, print " (n) is a deficient number "
    If the n equals EXIT number, print " Have a good one! "
    """
    print('Welcome to the number checker!')
    n = int(input('n: '))
    while n != EXIT:
        total = 0                                       # sum of every factor of n
        for i in range(1, n):                           # find factors of the n
            if n % i == 0:                              # if remainder = 0, i is a factor of n
                total = total + i                       # calculate sum of factors of n
        if total == n:
            print(str(n) + ' is a perfect number')
        elif total > n:
            print(str(n) + ' is a abundant number')
        else:
            print(str(n) + ' is a deficient number')
        n = int(input('n: '))
    print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
