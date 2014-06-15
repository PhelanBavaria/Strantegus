

import pygame
from common.tiles.tile import BaseTile


class ColonyWall(BaseTile):
    def __init__(self, world, colony, x, y):
        self.x = x
        self.y = y
        self.colony = colony
        BaseTile.__init__(self, world, 'colony_wall')
