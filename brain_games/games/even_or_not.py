#!/usr/bin/env python


from random import randint


def calculations():
    number = randint(1, 100)
    question = str(number)
    if number % 2 == 0:
        right_answer = 'yes'
        return question, right_answer
    else:
        right_answer = 'no'
        return question, right_answer


def game_actions():
    i = 0
    game_contents = []
    while i < 3:
        game_contents.append(calculations())
        i += 1
    return game_contents
