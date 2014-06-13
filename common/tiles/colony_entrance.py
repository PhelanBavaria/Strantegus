

import pygame
from common.tiles.tile import BaseTile


class ColonyEntrance(BaseTile):
    def __init__(self, world, x, y):
        self.x = x
        self.y = y
        BaseTile.__init__(self, world, 'colony_entrance')
