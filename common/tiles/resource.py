

import pygame
from config import TILE_SIZE
from common.tiles.tile import BaseTile
from common import resources


class Resource(BaseTile):
    def __init__(self, x, y, world, resource, level='surface'):
        BaseTile.__init__(self, x, y, world, resource)
        self.amount = TILE_SIZE*TILE_SIZE*5  # 5 layers
        self.name = resource
        world.resources.add(self)
        world.levels[level]['foreground'].add(self)

    def update(self):
        if self.amount == 0:
            self.kill()
        elif self.amount < 0:
            raise ValueError('Amount of resource '+str(self)+' below 0')

    def structure(self, amount):
        BaseTile.structure(self, amount, False)
