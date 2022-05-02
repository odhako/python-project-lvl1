#!/usr/bin/env python


from brain_games.game_start import game_start
from brain_games.games.gcd import round_generator, get_rules


def main():
    game_start(get_rules, round_generator)


if __name__ == '__main__':
    main()
