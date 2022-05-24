#!/usr/bin/env python


from brain_games.games import gcd
from brain_games import engine


def main():
    print(engine.play(gcd))


if __name__ == '__main__':
    main()
