"""
File: extension1_factorial.py
Name: Zoe
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    Ask user to enter a data(integer)
    If the data does not equal EXIT number, show factorial and print the Answer
    Otherwise print " ----- See ya! ----- "
    """
    print('Welcome to the stanCode factorial master!')
    data = int(input('Give me a number, and I will list the answer of factorial: '))
    while data != EXIT:
        show_factorial(data)
        data = int(input('Give me a number, and I will list the answer of factorial: '))
    print('----- See ya! -----')


def show_factorial(data):
    """
    :param data: int, the number to be calculated
    """
    ans = 1
    while data != 0:
        ans = ans * data
        data = data - 1
    print('Answer: ' + str(ans))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
