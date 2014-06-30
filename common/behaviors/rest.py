

from util.randop import one_in


def rand_time(ant):
    if one_in(4000):
        ant.colony.exit(ant)


def indefinite(ant):
    pass
