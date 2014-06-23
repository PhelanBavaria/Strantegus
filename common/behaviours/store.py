

import random


def default(ant):
    def same_ant_type(BaseEntity):
        return type(ant) == type(BaseEntity) and ant != BaseEntity
    ant.colony.store(ant.resource)
    ant.resource = None
    ant.colony.exit(ant)
    ant.behaviour = None
    ants = list(filter(same_ant_type, ant.world.levels['underground']['foreground']))
    for i in range(min(len(ants), 2)):
        recr_ant = random.choice(ants)
        ant.colony.exit(recr_ant)
        recr_ant.behaviour = ant.behaviour
        recr_ant.rect.center = ant.rect.center
        recr_ant.rotation = ant.rotation
