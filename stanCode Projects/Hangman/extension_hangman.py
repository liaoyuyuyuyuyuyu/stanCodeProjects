"""
File: hangman.py
Name: Zoe
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Create a hangman game.
    User only has "N_TURNS" chances to guess wrong.
    While guessing chance is not 0 and user has not guess the whole word right, let user guesses.
    Otherwise, show ending information.
    """
    secret = random_word()                                  # assign a random word to "secret"
    ans = setup(secret)                                     # print beginning info
    chance = N_TURNS                                        # assign N_TURNS to a variable
    while chance > 0 and ans != secret:                     # conditions when user can guess
        input_ch = input('Your guess: ')
        if input_ch.isalpha() and len(input_ch) == 1:       # check the format of "input_ch"
            upper_ch = input_ch.upper()                     # if format is right, make letter upper case
            if upper_ch in secret:                          # check if letter is in the word
                ans = update(secret, upper_ch, ans)         # update "ans"
                print('You are correct!')
            else:                                           # when letter is not in the word
                chance = chance - 1                         # guessing chance - 1
                print("There is no " + upper_ch + "'s in the word.")
                draw(chance)                                # show drawing only when guessing wrong
            if chance > 0 and ans != secret:                # conditions when user can guess
                print('The word looks like: ' + ans)
                print('You have ' + str(chance) + ' wrong guesses left.')
            else:                                           # otherwise, end the game
                ending(ans, secret)
        else:
            print('Illegal format.')


def setup(secret):
    """
    :param secret: str, the word that user should guess
    :return : str, show user how the word looks like
    """
    ans = ''
    for i in range(len(secret)):
        ans += '-'
    print('The word looks like: ' + ans)
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    return ans


def update(secret, upper_ch, ans):
    """
    :param secret: str, the word that user should guess
    :param upper_ch: str, the alphabet (upper case) that user enters
    :param ans: str, show user how the word looks like
    :return : str, show user how the word looks like
    """
    i = secret.find(upper_ch)                           # i is the index of the first "upper_ch" in secret
    ans = ans[:i] + upper_ch + ans[i + 1:]              # ans = 1st part + "upper_ch" + 2nd part
    add_index = 1                                       # When use specific part of word, should add numbers
    for a in range(len(secret[i + 1:])):                # Check every letter after the first "upper_ch"
        if upper_ch in secret[i + add_index:]:          # Start from the right of the "upper_ch"
            j = secret[i + add_index:].find(upper_ch)   # j is the index of "upper_ch" in 2nd part
            i = i + j + add_index                       # i is the index of the next "upper_ch" in secret
            ans = ans[:i] + upper_ch + ans[i + 1:]      # ans = 1st part + "upper_ch" + 2nd part
            add_index += 1                              # There are more "0" needed to be counted
    return ans


def draw(chance):
    print('▁▁▁▁▁▁▁▁')
    print('    ▎')
    if chance == N_TURNS:
        pass
    elif chance == N_TURNS-1:
        print('   ☹')
    elif chance == N_TURNS-2:
        print('   ☹')
        print('   |')
    elif chance == N_TURNS-3:
        print('   ☹')
        print('  /|')
    elif chance == N_TURNS-4:
        print('   ☹')
        print('  /|\\')
    elif chance == N_TURNS-5:
        print('   ☹')
        print('  /|\\')
        print('  /')
    elif chance == N_TURNS-6:
        print('   ☹')
        print('  /|\\')
        print('  / \\')
    else:
        print('   ☠')
        print('  /|\\')
        print('  / \\')


def ending(ans, secret):
    """
    :param ans: str, show user how the word looks like
    :param secret: str, the word that user should guess
    """
    if ans == secret:
        print('You win!!')
    else:
        print('You are completely hung :(')
    print('The answer is: ' + secret)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
