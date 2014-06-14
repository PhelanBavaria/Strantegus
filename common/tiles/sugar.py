

import pygame
from config import TILE_SIZE
from common.tiles.tile import BaseTile
from common import resources


class Sugar(BaseTile):
    def __init__(self, world, x, y, level='surface'):
        self.x = x
        self.y = y
        BaseTile.__init__(self, world, 'sugar')
        self.amount = TILE_SIZE
        self.name = 'sugar'
        world.resources.add(self)
        world.levels[level][1].add(self)

    def update(self):
        if self.amount == 0:
            self.kill()
        elif self.amount < 0:
            raise ValueError('Amount of resource '+str(self)+' below 0')
