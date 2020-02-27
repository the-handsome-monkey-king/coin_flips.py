#!/usr/bin/env python
"""coin_flips.py

Simulate coin flips and record the number of heads and tails."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

from random import randint
import sys

def main():
    try:
        n = (int)(sys.argv[1])
        if n < 1:
            raise ValueError
    except(ValueError, IndexError):
        print("Usage: coin_flips.py [n]")
        print("[n] = the number of times to flip a coin, int greater than 0")
        sys.exit(1)

    heads = 0
    tails = 0
    for i in range(n):
        x = randint(0, 1)
        if x == 0:
            heads += 1
        else:
            tails += 1

    print("Times Flipped: {}".format(n))
    print("Heads: {}".format(heads))
    print("Tails: {}".format(tails))

if __name__ == "__main__":
    main()
