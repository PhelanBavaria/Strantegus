

import random


def default(ant):
    def same_ant_type(entity):
        return type(ant) == type(entity) and ant != entity
    ant.colony.store(ant.resource)
    ant.resource = None
    ant.colony.exit(ant)
    ant.behaviour = None
    ants = list(filter(same_ant_type, ant.colony.in_ants))
    for i in range(min(len(ants), 2)):
        recr_ant = random.choice(ants)
        ant.colony.exit(recr_ant)
        recr_ant.behaviour = ant.behaviour
        recr_ant.rect.center = ant.rect.center
        recr_ant.rotation = ant.rotation
