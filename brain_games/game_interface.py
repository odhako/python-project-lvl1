#!/usr/bin/env python


import prompt


def game_interface(game_rules, game_actions):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game_rules())
    number_of_games = 3
    i = 0
    while i < number_of_games:
        question, right_answer = game_actions()
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
    if i == number_of_games:
        print('Congratulations, ' + name + '!')
