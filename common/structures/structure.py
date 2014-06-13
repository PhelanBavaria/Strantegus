

import pygame


class BaseStructure:
    def __init__(self, world, tile=None, size=5, auto_increment=0):
        self.world = world
        self.tile = tile
        self.tiles = pygame.sprite.Group()
        self.size = size
        self.auto_increment = auto_increment
        world.structures.add(self)

    def update(self):
        if self.auto_increment:
            self.size += self.auto_increment
            self.increase()

    def increase(self):
        tile = self.tile()
        self.tiles.add(tile)
