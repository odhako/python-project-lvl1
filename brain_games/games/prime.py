#!/usr/bin/env python


from random import randint


def is_a_prime(x):
    divider = 2
    if x == 1:
        return True
    while x / 2 >= divider:
        if x % divider == 0:
            return False
        else:
            divider += 1
    return True


def calculations():
    number = randint(1, 100)
    question = str(number)
    if is_a_prime(number):
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
