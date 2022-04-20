#!/usr/bin/env python


from random import randint


def get_rules():
    return 'What number is missing in the progression?'


def round_generator():
    start = randint(1, 20)
    step = randint(1, 5)
    progression = ''
    progression += f'{start} '
    i = 1
    blank_step = randint(1, 10)
    while i < 11:
        if i == blank_step:
            right_answer = (start + (i * step))
            progression += '.. '
            i += 1
        else:
            progression += f'{start + (i * step)} '
            i += 1
    return progression, str(right_answer)
