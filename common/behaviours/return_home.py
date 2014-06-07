

from pygame.sprite import spritecollide
from common.scents import AntScent


def direct(ant):
    objects = spritecollide(ant, ant.world.objects, False)
    if ant.colony in objects:
        ant.colony.enter(ant)
    else:
        ant.move(ant.colony.rect.center)
        if ant.ressource and not ant.world.current_tick % 4:
            AntScent(ant, 'ressource')
