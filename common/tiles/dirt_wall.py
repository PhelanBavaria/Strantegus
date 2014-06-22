

import pygame
from common.tiles.tile import BaseTile


class DirtWall(BaseTile):
    def __init__(self, world, colony, x, y):
        self.colony = colony
        BaseTile.__init__(self, x, y, world, 'dirt_wall')
        self.passable = False
        world.levels['underground'][0].add(self)
        world.obstacles.add(self)
