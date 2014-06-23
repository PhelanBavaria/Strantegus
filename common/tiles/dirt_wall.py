

import pygame
from common.tiles.tile import BaseTile


class DirtWall(BaseTile):
    def __init__(self, world, x, y, level='underground'):
        BaseTile.__init__(self, x, y, world, 'dirt_wall')
        self.passable = False
        world.levels[level][0].add(self)
        world.obstacles.add(self)
