

import pygame
from common.tiles.tile import BaseTile


class Dirt(BaseTile):
    def __init__(self, world, colony, x, y):
        self.colony = colony
        BaseTile.__init__(self, x, y, world, 'dirt')
        world.levels['underground'][0].add(self)
