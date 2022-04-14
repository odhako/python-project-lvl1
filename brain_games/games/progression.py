#!/usr/bin/env python


from random import randint


def calculations():
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
    return progression, right_answer


def game_actions():
    i = 0
    game_contents = []
    while i < 3:
        game_contents.append(calculations())
        i += 1
    return game_contents
