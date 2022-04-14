#!/usr/bin/env python


from brain_games.game_interface import game_interface
from brain_games.games.progression import game_actions


game_rules = 'What number is missing in the progression?'


def main():
    game_contains = game_actions()
    game_interface(game_rules, game_contains)


if __name__ == '__main__':
    main()
