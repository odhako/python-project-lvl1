#!/usr/bin/env python


from brain_games.game_interface import game_interface
from brain_games.games.gcd import game_actions, game_rules


def main():
    game_interface(game_rules, game_actions)


if __name__ == '__main__':
    main()
