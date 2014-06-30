

import random
import pygame
from util.randop import rand_rgb
from config import SCENT_UPDATE_TICKS
from config import TILE_SIZE
from common.markers import BaseMarker


class Scent(BaseMarker):
    def __init__(self, ant, kind, amount=20):
        x, y = ant.rect.center
        BaseMarker.__init__(self, ant.world, x, y, alpha=amount)
        self.x = ant.rect.x//TILE_SIZE*TILE_SIZE
        self.y = ant.rect.y//TILE_SIZE*TILE_SIZE
        self.kind = kind

        existing = self.exists(ant)
        if existing:
            existing.amount += amount
            existing.ants.add(ant)
            self.delete()
        else:
            self.ants = pygame.sprite.Group(ant)
            self.colony = ant.colony
            self.nation = ant.nation
            self.amount = amount
            self.last_update = ant.world.current_tick
            ant.scents.add(self)
            ant.colony.scents.add(self)
            ant.nation.scents.add(self)
            if kind not in ant.world.scents.keys():
                ant.world.scents[kind] = pygame.sprite.Group()
                self.color = rand_rgb()
            else:
                self.color = list(ant.world.scents[kind])[0].color
            ant.world.scents[kind].add(self)

    def exists(self, ant):
        for scent in ant.colony.scents:
            on_same_position = (scent.x, scent.y) == (self.x, self.y)
            of_same_type = scent.kind == self.kind
            if on_same_position and of_same_type:
                return scent

    def update(self):
        if self.last_update < self.world.current_tick:
            ticks_passed = self.world.current_tick - self.last_update
            self.amount -= ticks_passed / SCENT_UPDATE_TICKS
            self.alpha = self.amount
            self.last_update = self.world.current_tick
        if self.amount <= 0:
            self.delete()
