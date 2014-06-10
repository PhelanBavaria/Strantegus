

import pygame
from common.tiles.base import Tile
from util.load import load_image


class Grass(Tile):
    def __init__(self, world, x, y):
        self.image = load_image('grass.bmp')#, -1)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        Tile.__init__(self, world)
