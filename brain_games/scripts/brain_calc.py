#!/usr/bin/env python


from brain_games.game_start import game_start
from brain_games.games.calculator import generate_round, RULES


def main():
    game_start(RULES, generate_round)


if __name__ == '__main__':
    main()
