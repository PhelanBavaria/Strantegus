

from pygame.sprite import spritecollide
from common.tiles import scents


def direct(ant):
    objects = spritecollide(ant, ant.world.tiles, False)
    for entrance in ant.colony.entrances:
        if entrance in objects:
            ant.colony.enter(ant)
            return
    ant.move(ant.exit_hole.rect.center)
    if ant.resource and not ant.world.current_tick % 4:
        scents.Resource(ant)
        #AntScent(ant, 'resource')
