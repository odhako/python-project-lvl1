#!/usr/bin/env python


from random import randint


def calc_gcd(x, y):
    i = 1
    dividers = []
    while i < x or i < y:
        if x % i == 0 and y % i == 0:
            dividers.append(i)
            i += 1
        else:
            i += 1
    return(max(dividers))


def calculations():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = f'{number_1}, {number_2}'
    right_answer = calc_gcd(number_1, number_2)
    return question, right_answer


def game_actions():
    i = 0
    game_contents = []
    while i < 3:
        game_contents.append(calculations())
        i += 1
    return game_contents
