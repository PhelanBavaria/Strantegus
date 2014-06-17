

import random


def rand_time(ant):
    if 1 == random.randint(1, 4000):
        ant.colony.exit(ant)
        ant.behaviour = None  # ToDo: remove this and adjust other code


def indefinite(ant):
    pass
