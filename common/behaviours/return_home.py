

from pygame.sprite import spritecollide
from common.scents import AntScent


def direct(self, ant):
        objects = spritecollide(ant, ant.world.objects, False)
        if ant.colony in objects:
            ant.colony.enter(ant)
        else:
            ant.move(ant.colony.rect.center)
            AntScent(ant)
            if self.ressource:
                AntScent(ant, 30)
