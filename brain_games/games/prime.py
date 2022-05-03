from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divider = 2
    if number == 1:
        return False
    while number / 2 >= divider:
        if number % divider == 0:
            return False
        else:
            divider += 1
    return True


NUMBER_MIN = 1
NUMBER_MAX = 100


def generate_round():
    number = randint(NUMBER_MIN, NUMBER_MAX)
    question = str(number)
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, str(right_answer)
