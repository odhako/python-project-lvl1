#!/usr/bin/env python


from random import randint, choice


def game_rules():
    return 'What is the result of the expression?'


def game_actions():
    number_1 = randint(1, 30)
    number_2 = randint(1, 30)
    operation = choice(['+', '-', '*'])
    if operation == '+':
        question = f'{number_1} + {number_2}'
        right_answer = number_1 + number_2
    elif operation == '-':
        question = f'{number_1} - {number_2}'
        right_answer = number_1 - number_2
    elif operation == '*':
        question = f'{number_1} * {number_2}'
        right_answer = number_1 * number_2
    else:
        question = ''
        right_answer = 0
    return question, str(right_answer)
