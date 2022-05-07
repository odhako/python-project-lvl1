from random import randint, choice


RULES = 'What is the result of the expression?'


NUMBER_MIN = 1
NUMBER_MAX = 30


def generate_round():
    number_1 = randint(NUMBER_MIN, NUMBER_MAX)
    number_2 = randint(NUMBER_MIN, NUMBER_MAX)
    operation = choice(['+', '-', '*'])
    question = f'{number_1} {operation} {number_2}'
    if operation == '+':
        right_answer = number_1 + number_2
    elif operation == '-':
        right_answer = number_1 - number_2
    elif operation == '*':
        right_answer = number_1 * number_2
    else:
        question = ''
        right_answer = 'Error'
    return question, str(right_answer)
