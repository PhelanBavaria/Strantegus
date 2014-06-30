

import pygame
from config import SCENT_UPDATE_TICKS
from common.markers import BaseMarker


class Scent(BaseMarker):
    def __init__(self, ant, amount=20):
        BaseMarker.__init__(self, ant.world, *ant.rect.center)
        self.ant = ant
        self.amount = amount
        self.initiated = ant.world.current_tick
        self.last_update = self.initiated
        ant.scents.add(self)
        ant.colony.scents.add(self)
        ant.nation.scents.add(self)

    def update(self):
        if self.last_update < self.world.current_tick:
            ticks_passed = self.world.current_tick - self.last_update
            self.amount -= ticks_passed / SCENT_UPDATE_TICKS
            self.last_update = self.world.current_tick
        if self.amount <= 0:
            self.delete()
