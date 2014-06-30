

from pygame.sprite import spritecollide
from common.markers import Scent


def direct(ant):
    entrances = spritecollide(ant, ant.colony.entrances, False)
    if entrances:
        ant.colony.enter(ant)
    else:
        ant.move(ant.exit_hole.rect.center)
        if ant.resource and not ant.world.current_tick % 4:
            Scent(ant)
