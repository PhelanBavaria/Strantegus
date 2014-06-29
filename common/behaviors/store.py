

import random


def default(ant):
    def same_ant_type(BaseEntity):
        return type(ant) == type(BaseEntity) and ant != BaseEntity
    def same_job(entity):
        return ant.job == entity.job
    ant.colony.store(ant.resource)
    ant.resource = None
    ant.colony.exit(ant)
    ant.behavior = None
    ants = list(filter(same_ant_type, ant.world.levels['underground']['foreground']))
    ants = list(filter(same_job, ants))
    for i in range(min(len(ants), 2)):
        recr_ant = random.choice(ants)
        ant.colony.exit(recr_ant)
        recr_ant.behavior = ant.behavior
        recr_ant.rect.center = ant.rect.center
        recr_ant.rotation = ant.rotation
