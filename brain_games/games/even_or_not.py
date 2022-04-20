#!/usr/bin/env python


from random import randint


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def round_generator():
    number = randint(1, 100)
    question = str(number)
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, str(right_answer)
