

import pygame
from common.tiles.base import Tile


class Grass(Tile):
    def __init__(self, world, x, y):
        self.x = x
        self.y = y
        Tile.__init__(self, world, 'grass')
