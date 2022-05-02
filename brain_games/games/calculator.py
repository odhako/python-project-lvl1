from random import randint, choice


RULES = 'What is the result of the expression?'


NUMBER_MIN = 1
NUMBER_MAX = 30


def round_generator():
    number_1 = randint(NUMBER_MIN, NUMBER_MAX)
    number_2 = randint(NUMBER_MIN, NUMBER_MAX)
    operation = choice(['+', '-', '*'])
    if operation == '+':
        question = f'{number_1} + {number_2}'
        right_answer = number_1 + number_2
    elif operation == '-':
        question = f'{number_1} - {number_2}'
        right_answer = number_1 - number_2
    elif operation == '*':
        question = f'{number_1} * {number_2}'
        right_answer = number_1 * number_2
    else:
        question = ''
        right_answer = 0
    return question, str(right_answer)
