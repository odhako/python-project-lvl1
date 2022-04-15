#!/usr/bin/env python


from random import randint


def game_rules():
    return 'What is the result of the expression?'


def game_actions():
    number_1 = randint(1, 30)
    number_2 = randint(1, 30)
    operation = randint(1, 3)
    if operation == 1:
        question = f'{number_1} + {number_2}'
        right_answer = number_1 + number_2
        return question, right_answer
    elif operation == 2:
        question = f'{number_1} - {number_2}'
        right_answer = number_1 - number_2
        return question, right_answer
    elif operation == 3:
        question = f'{number_1} * {number_2}'
        right_answer = number_1 * number_2
        return question, right_answer
