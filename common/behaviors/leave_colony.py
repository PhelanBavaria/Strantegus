

from util.randop import one_in


def randomly(ant):
    if one_in(4000):
        ant.colony.exit(ant)


def recruited(ant):    
