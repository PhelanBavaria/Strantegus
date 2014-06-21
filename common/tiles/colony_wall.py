

import pygame
from common.tiles.tile import BaseTile


class ColonyWall(BaseTile):
    def __init__(self, world, colony, x, y):
        self.colony = colony
        BaseTile.__init__(self, x, y, world, 'colony_wall')
        world.levels['surface'][0].add(self)
