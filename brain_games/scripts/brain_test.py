#!/usr/bin/env python


from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    # welcome_user()
    name = welcome_user()
    print('This is test of name: ' + name)


if __name__ == '__main__':
    main()
