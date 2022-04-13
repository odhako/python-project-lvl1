#!/usr/bin/env python


import prompt
from brain_games.cli import enter_name


def game_interface(game_rules, game_contains):
    print('Welcome to the Brain Games!')
    name = enter_name()
    print(game_rules)
    i = 0
    while i < 3:
        question, right_answer = game_contains[i]
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if str(answer) == str(right_answer):
            print('Correct!')
            i += 1
        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer was {right_answer}")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print('Congratulations, ' + name + '!')
