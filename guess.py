# This is a guessing game good luck!
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randit(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')