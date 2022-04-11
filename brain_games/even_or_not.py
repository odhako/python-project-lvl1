#!/usr/bin/env python


import prompt
from random import randint


def even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = randint(1, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and str.lower(answer) == 'yes':
            print('Correct!')
            i += 1
        elif number % 2 == 1 and str.lower(answer) == 'no':
            print('Correct!')
            i += 1
        else:
            if number % 2 == 0:
                print(str(answer) + " is wrong answer ;(. Correct answer was 'yes'.")
            else:
                print(str(answer) + " is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + '!')
            break
    if i == 3:
        print('Congratulations, ' + name + '!')