from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


NUMBER_MIN = 1
NUMBER_MAX = 100


def generate_round():
    number = randint(NUMBER_MIN, NUMBER_MAX)
    question = str(number)
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, str(right_answer)
