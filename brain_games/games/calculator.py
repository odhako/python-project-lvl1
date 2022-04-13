#!/usr/bin/env python


from random import randint


def calculations():
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


def game_actions():
    i = 0
    game_contents = []
    while i < 3:
        game_contents.append(calculations())
        i += 1
    return game_contents
