#!/usr/bin/env python


from brain_games.games import prime
from brain_games import engine


def main():
    print(engine.play(prime))


if __name__ == '__main__':
    main()
