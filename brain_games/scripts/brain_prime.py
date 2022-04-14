#!/usr/bin/env python


from brain_games.game_interface import game_interface
from brain_games.games.prime import game_actions


game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    game_contains = game_actions()
    game_interface(game_rules, game_contains)


if __name__ == '__main__':
    main()
