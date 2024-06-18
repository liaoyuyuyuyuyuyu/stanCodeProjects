"""
File: caesar.py
Name: Zoe
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Ask a secret number (times of shift)
    Ask a string to be encrypted
    Start to decipher
    """
    secret = int(input('Secret number: '))
    message = input("What's the ciphered string? ")
    decipher(secret, message)


def decipher(secret, message):
    """
    :param secret: int, times of shift
    :param message: string, string to be encrypted
    Create a new empty string
    Put the second part of [ALPHABET] to be the first part of [new_alphabet]
    Put the first part of [ALPHABET] to be the second part of [new_alphabet]
    """
    new_alphabet = ''
    new_alphabet += ALPHABET[26-secret:]
    new_alphabet += ALPHABET[:26-secret]
    result = ''
    for i in range(len(message)):
        ch = message[i]                                 # Record the character
        if ch.isalpha():                                # If ch is an alphabet,
            upper_ch = ch.upper()                       # Make ch upper case
            a = new_alphabet.find(upper_ch)             # Record the index of ch in [new_alphabet]
            result += new_alphabet[(a+secret) % 26]     # Add the deciphered alphabet to the string
        else:
            result += ch                                # Otherwise, add ch to the string
    print('The deciphered string is: ' + result)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
