

import random
import pygame
from pygame.sprite import spritecollide
import config
from util.id_generator import id_generator
from common.entities import Ant


class Larvae(Ant):
    def __init__(self, world, colony):
        Ant.__init__(self, world, colony.leader.nation)
        self.colony = colony

    def behave_check(self):
        if self.age <= 80:
            self.hatch(self.hatching_type())

    def hatching_type(self):
        return Ant

    def hatch(self, ant_type):
        ant = ant_type(self.world, self.nation, self.scent)
        ant.rect.center = self.rect.center
        self.colony.join(ant)
        self.kill()
