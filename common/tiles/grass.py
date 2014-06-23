

import pygame
from common.tiles.tile import BaseTile


class Grass(BaseTile):
    def __init__(self, world, x, y):
        BaseTile.__init__(self, x, y, world, 'grass')
        world.levels['surface']['background'].add(self)
