#!/usr/bin/env python


from brain_games.game_interface import game_interface
from brain_games.games.even_or_not import round_generator, get_rules


def main():
    game_interface(get_rules, round_generator)


if __name__ == '__main__':
    main()
