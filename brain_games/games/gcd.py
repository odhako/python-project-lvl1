#!/usr/bin/env python


from random import randint


def game_rules():
    return 'Find the greatest common divisor of given numbers.'


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


def game_actions():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = f'{number_1} {number_2}'
    right_answer = calc_gcd(number_1, number_2)
    return question, right_answer
