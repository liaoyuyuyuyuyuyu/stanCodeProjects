"""
File: hailstone.py
Name: Zoe
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    First, ask an number.
    If the number equals 1, end this program.
    If the number is even; then, divide it by two, print information, start a new "while check."
    If the number is odd; then, multiply it by 3 then + 1, print information, start a new "while check."
    Everytime before ending a while loop, "step" needs to +1 and num needs to be assigned to "new num"
    """
    print('This program computes Hailstone sequences.')
    num = int(input('Enter a number: '))
    step = 0
    while num != 1:
        if num % 2 == 0:        # if num is even
            new = num // 2
            print(str(num) + ' is even, so I take half: ' + str(new))
        else:
            new = 3 * num + 1
            print(str(num) + ' is odd, so I make 3n+1: ' + str(new))
        num = new
        step = step + 1
    print('It took ' + str(step) + ' steps to reach 1')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
