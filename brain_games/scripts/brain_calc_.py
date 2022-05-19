#!/usr/bin/env python


from brain_games.games import calc
from brain_games import game_frame


def main():
    print(game_frame.play(calc))


if __name__ == '__main__':
    main()
