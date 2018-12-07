#!/usr/bin/env python3

from os.path import dirname, realpath

import getopt
import sys

import core.hookloader

from entry import SothothInstance, Component

sys.path.insert(0, f"{dirname(realpath(__file__))}/..")

from plugins import sothoth_loader

#import sothoth_loader

# print wrapper for stderror
def perror(error, *objects, end='\n', **kwargs):
    print(*objects, file=sys.stderr, **kwargs, end=f" - {type(error).__name__}: {error}.{end}")

def usage():
    print(
        "sothoth"
    )

def main():
    try:
        optarg, floating = getopt.getopt(
            sys.argv[1:],
            "h",
            [
                "help"
            ]
        )
    
    except getopt.GetoptError as e:
        perror(e, "Getopt error")
        return 1
    
    """
    initialize Sothoth instance and load core command hooks, followed by loading plugins
    """

    sothoth = SothothInstance()

    try:
        core.hookloader.load_into(sothoth)
    except ValueError as e:
        perror(e, "A naming conflict has occurred while loading src/core")

    
    return 1


if __name__ == "__main__":
    sys.exit(main())
