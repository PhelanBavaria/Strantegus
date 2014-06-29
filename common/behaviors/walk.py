

import random


def random_walk(ant):
    if 1 == random.randint(1, 50):
        ant.rand_rotate()
    ant.move()
