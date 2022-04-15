#!/usr/bin/env python


from random import randint


def game_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def game_actions():
    number = randint(1, 100)
    question = str(number)
    if number % 2 == 0:
        right_answer = 'yes'
        return question, right_answer
    else:
        right_answer = 'no'
        return question, right_answer
