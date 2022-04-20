#!/usr/bin/env python


from random import randint


def get_rules():
    return 'Find the greatest common divisor of given numbers.'


def calc_gcd(number_1, number_2):
    i = 1
    dividers = []
    while i <= number_1 or i <= number_2:
        if number_1 % i == 0 and number_2 % i == 0:
            dividers.append(i)
            i += 1
        else:
            i += 1
    return(max(dividers))


NUMBER_MIN = 1
NUMBER_MAX = 100


def round_generator():
    number_1 = randint(NUMBER_MIN, NUMBER_MAX)
    number_2 = randint(NUMBER_MIN, NUMBER_MAX)
    question = f'{number_1} {number_2}'
    right_answer = calc_gcd(number_1, number_2)
    return question, str(right_answer)
