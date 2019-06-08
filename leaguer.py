#!/usr/bin/env python
import sys
from models.game import Game


def main():
    game = Game()

    if len(sys.argv) > 1:
        # Read game results from file
        f = open(sys.argv[1], "r")
        for x in f:
            game.register_game(x)
        f.close()
    else:
        # Read game results from input strings
        text_in = input()
        while text_in:
            game.register_game(text_in)
            text_in = input()

    game.print()


if __name__ == "__main__":
    main()
