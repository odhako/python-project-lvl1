#!/usr/bin/env python


from brain_games.game_interface import game_interface
from brain_games.games.even_or_not import game_actions


game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    game_contains = game_actions()
    game_interface(game_rules, game_contains)


if __name__ == '__main__':
    main()
