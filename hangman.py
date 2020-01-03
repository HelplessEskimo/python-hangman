# basic hangman implimentation in python

from random import choice
import os

words = [
    "adventure",
    "dependence",
    "heel",
    "collapse",
    "establish",
    "decline",
    "press",
    "glass",
    "unpleasant",
    "cafe",
    "shareholder",
    "therapist",
    "withdraw",
    "earthquake",
    "institution",
    "broadcast",
    "tradition",
    "perform",
    "exile",
    "economic"
]

os.system('clear')

name = input("What is you name?\n> ")

print("Hello %s!\n" % name)


def draw_word(secret_word, length, replace, indexes, replacement):
    if replace is True:
        s = list(secret_word)
        for index in indexes:
            s[index] = replacement
        secret_word = ''.join(s)
    else:
        secret_word = secret_word.join('_' for x in range(length))
    return secret_word


def check_word(char, word, secret_word):
    string_to_check = list(word)
    if char in string_to_check:
        if char not in secret_word:
            index = [i for i, x in enumerate(string_to_check) if x == char]
            return index
        else:
            print("you already chose this letter")
            return []
    else:
        return "wrong"


def check_win(secret_word):
    if "_" not in secret_word:
        print("you win!")
        return True
    else:
        return False


def game():
    word = choice(words)
    secret = ''

    length = len(word)
    lives = 3
    secret = draw_word(secret, length, False, [], [])
    print(secret, end="\r", flush=True)

    while lives > 0:
        win_state = check_win(secret)
        if win_state is True:
            break
        else:
            char = input("\n")
            index = check_word(char, word, secret)
            if index == "wrong":
                lives -= 1
                new_secret = secret
            else:
                new_secret = draw_word(secret, length, True, index, char)

            secret = new_secret
            print(secret, end="\r", flush=True)
    if lives == 0:
        print("you lose, the word was %s" % word)


game()
print("\n")
# print("there are %s letters in the word" % str(len(word)))
