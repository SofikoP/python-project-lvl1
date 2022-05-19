#!/usr/bin/env python


from brain_games.games import gcd
from brain_games import game_frame


def main():
    print(game_frame.play(gcd))


if __name__ == '__main__':
    main()
