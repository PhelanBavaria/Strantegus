

import pygame
from common.tiles.tile import BaseTile


class ColonyEntrance(BaseTile):
    def __init__(self, world, colony, x, y):
        self.x = x
        self.y = y
        self.colony = colony
        BaseTile.__init__(self, world, 'colony_entrance')
        colony.entrances.add(self)
