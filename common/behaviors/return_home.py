

from pygame.sprite import spritecollide
from common.markers import Scent


def follow_trail(ant):
    entrances = spritecollide(ant, ant.colony.entrances, False)
    if entrances:
        ant.colony.enter(ant)
    else:
        waypoints = ant.home_path[:]
        waypoints.reverse()
        try:
            if ant.rect.collidepoint(*ant.home_path[-1]):
                ant.home_path.pop(-1)
            ant.move(ant.home_path[-1])
        except IndexError:
            ant.move(ant.exit_hole.rect.center)
        if ant.resource and not ant.world.current_tick % 4:
            Scent(ant, 'resource')


def direct(ant):
    entrances = spritecollide(ant, ant.colony.entrances, False)
    if entrances:
        ant.colony.enter(ant)
    else:
        ant.move(ant.exit_hole.rect.center)
        if ant.resource and not ant.world.current_tick % 4:
            Scent(ant, 'resource')
