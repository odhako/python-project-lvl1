from random import randint


RULES = 'What number is missing in the progression?'


START_MIN = 1
START_MAX = 20
STEP_MIN = 1
STEP_MAX = 5
PROGRESSION_LENGTH = 10


def round_generator():
    start = randint(START_MIN, START_MAX)
    step = randint(STEP_MIN, STEP_MAX)
    progression = ''
    i = 1
    blank_step = randint(1, PROGRESSION_LENGTH)
    while i <= PROGRESSION_LENGTH:
        if i == blank_step:
            right_answer = (start + (i * step))
            progression += '.. '
            i += 1
        else:
            progression += f'{start + (i * step)} '
            i += 1
    return progression, str(right_answer)
