# basic hangman implimentation in python

from random import choice

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

name = input("What is you name?\n> ")

print("Hello %s!" % name)

word = choice(words)