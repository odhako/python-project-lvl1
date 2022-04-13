#!/usr/bin/env python


from brain_games.game_interface import game_interface
from brain_games.games.calculator import game_actions


game_rules = 'What is the result of the expression?'


def main():
    game_contains = game_actions()
    game_interface(game_rules, game_contains)


if __name__ == '__main__':
    main()
