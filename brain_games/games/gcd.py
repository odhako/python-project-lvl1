#!/usr/bin/env python


from random import randint


def game_rules():
    return 'Find the greatest common divisor of given numbers.'


def calc_gcd(number_1, number_2):
    i = 1
    dividers = []
    while i < number_1 or i < number_2:
        if number_1 % i == 0 and number_2 % i == 0:
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
    return question, str(right_answer)
