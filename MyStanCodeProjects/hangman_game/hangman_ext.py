"""
File: hangman_ext.py
Name: Evonne
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
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
    This program plays hangman game and players have 7 rounds chance to figure the un-dashed word out.
    The program will identify whether the player input is correct or not and show updated word on console if correct,
    or display the part of hangman one by one if wrong within 7 rounds chance.
    """
    r = random_word()
    n = N_TURNS
    ans = str('-') * len(r)  # This is the pre_ans.

    while n > 0:
        print('The word looks like ' + ans)
        print('You have '+str(n)+' wrong guesses left.')
        display_hangman(n)
        input_ch = input('Your guess: ')
        # To check whether the input format is legal or not.
        if len(input_ch) == 1 and input_ch.isalpha():  # Legal format.
            input_ch1 = input_ch.upper()
            # To check whether the input character exists in the answer or not.
            if r.find(input_ch1) != -1:  # If exist.
                print('You are correct!')
                ans = replace(r, ans, input_ch1)
                if ans == r:  # If the answer is completed, then set n to 0 to end the loop.
                    n = 0
            else:
                n -= 1  # If not exist.
                print("There is no "+input_ch+"\'s in the word")
        else:
            print('Illegal format.')
    if ans == r:
        print('You win!!')
        print('The word was: '+r)
    else:
        print('You are completely hung : (')
        display_hangman(n)
        print('The word was: ' + r)


def replace(ans, pre_ans, correct_word):
    """
    :param ans: The correct answer.
    :param pre_ans: The previous answer, which uses dashes at beginning and saves the correct character from last time.
    :param correct_word: The user's input character.
    :return: The replaced answer, which was put the character into corresponding position of the current answer string.
    """
    replaced_ans = ""
    for i in range(len(pre_ans)):
        if ans[i] == correct_word:
            replaced_ans += correct_word
        else:
            replaced_ans += pre_ans[i]
    return replaced_ans


def display_hangman(n):
    if n == 7:
        print('＿＿＿')
        print('│   ｜')
        print('│')
        print('│')
        print('│')
        print('│')
        print('﹌﹌﹌﹌﹌')
    elif n == 6:
        print('＿＿＿')
        print('│   ｜')
        print('│   ○')
        print('│')
        print('│')
        print('│')
        print('﹌﹌﹌﹌﹌')
    elif n == 5:
        print('＿＿＿')
        print('│   ｜')
        print('│   ○')
        print('│   ｜')
        print('│')
        print('│')
        print('﹌﹌﹌﹌﹌')
    elif n == 4:
        print('＿＿＿')
        print('│   ｜')
        print('│   ○')
        print('│  /｜')
        print('│')
        print('│')
        print('﹌﹌﹌﹌﹌')
    elif n == 3:
        print('＿＿＿')
        print('│   ｜')
        print('│   ○')
        print('│  /｜\\')
        print('│')
        print('│')
        print('﹌﹌﹌﹌﹌')
    elif n == 2:
        print('＿＿＿')
        print('│   ｜')
        print('│   ○')
        print('│  /｜\\')
        print('│   /')
        print('│')
        print('﹌﹌﹌﹌﹌')
    elif n == 1:
        print('＿＿＿')
        print('│   ｜')
        print('│   ○')
        print('│  /｜\\')
        print('│   /\\')
        print('│')
        print('﹌﹌﹌﹌﹌')
    elif n == 0:
        print('＿＿＿')
        print('│   ｜')
        print('│   ◎')
        print('│  /｜\\')
        print('│   /\\')
        print('│')
        print('﹌﹌﹌﹌﹌')


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
