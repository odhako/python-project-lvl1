#!/usr/bin/env python


from random import randint


def game_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_a_prime(number):
    divider = 2
    if number == 1:
        return True
    while number / 2 >= divider:
        if number % divider == 0:
            return False
        else:
            divider += 1
    return True


def game_actions():
    number = randint(1, 100)
    question = str(number)
    if is_a_prime(number):
        right_answer = 'yes'
        return question, right_answer
    else:
        right_answer = 'no'
        return question, right_answer
