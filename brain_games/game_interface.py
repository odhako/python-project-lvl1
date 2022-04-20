#!/usr/bin/env python


import prompt


ROUND_COUNT = 3


def game_interface(get_rules, round_generator):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(get_rules())
    i = 0
    while i < ROUND_COUNT:
        question, right_answer = round_generator()
        print('Question: ' + question)
        answer = str.lower(prompt.string('Your answer: '))
        if answer == right_answer:
            print('Correct!')
            i += 1
        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer was {right_answer}")
            print(f"Let's try again, {name}!")
            break
    else:
        print('Congratulations, ' + name + '!')
