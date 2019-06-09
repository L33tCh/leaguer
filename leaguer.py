#!/usr/bin/env python
import sys
from models.game import Game


def main():
    game = Game()
    if len(sys.argv) > 1:
        # Read game results from file
        try:
            f = open(sys.argv[1], "r")
            for x in f:
                game.register_game(x)
            f.close()
        except:
            print("Problem reading file")
    else:
        # Read game results from input strings
        try:
            text_in = input("Enter game results in the expected format (<team1 score1, team2 score2) "
                            "and enter a blank line to end and calculate scores:\n")
            while text_in:
                game.register_game(text_in)
                text_in = input()
        except:
            print("Problem reading input")

    game.print()


if __name__ == "__main__":
    main()
