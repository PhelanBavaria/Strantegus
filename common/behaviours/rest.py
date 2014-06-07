

import random


def rand_time(ant):
    if 1 == random.randint(1, 4000):
        ant.colony.exit(ant)
        ant.behaviour = None


def indefinite(ant):
    pass
