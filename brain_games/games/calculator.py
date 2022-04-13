#!/usr/bin/env python


from random import randint
import prompt
from brain_games.cli import enter_name


def calc():
    print('Welcome to the Brain Games!')
    name = enter_name()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        number_1 = randint(1, 30)
        number_2 = randint(1, 30)
        operation = randint(1, 3)
        if operation == 1:
            question = f'{number_1} + {number_2}'
            right_answer = number_1 + number_2
        elif operation == 2:
            question = f'{number_1} - {number_2}'
            right_answer = number_1 - number_2
        elif operation == 3:
            question = f'{number_1} * {number_2}'
            right_answer = number_1 * number_2
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if str(answer) == str(right_answer):
            print('Correct!')
            i += 1
        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer was {right_answer}")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print('Congratulations, ' + name + '!')
