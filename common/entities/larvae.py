

import random
import pygame
from common.entities import Ant
from common.entities import Worker
from common.entities import Warrior


class Larvae(Ant):
    __slots__ = []

    def __init__(self, world, colony):
        Ant.__init__(self, world, colony.leader.nation)
        self.colony = colony

    def behave_check(self):
        if self.age <= 80:
            self.hatch(self.hatching_type())

    def hatching_type(self):
        if 1 == random.randint(1, 10):
            ant_type = Warrior
        else:
            ant_type = Worker
        return ant_type

    def hatch(self, ant_type):
        ant = ant_type(self.world, self.nation, self.scent)
        ant.rect.center = self.rect.center
        self.colony.join(ant)
        self.kill()
