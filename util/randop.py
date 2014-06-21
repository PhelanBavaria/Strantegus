

import random


def weighted_choice(weights, choices):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return choices[i]
    raise ValueError('Function has to return value, \
check if weights are not negative')
