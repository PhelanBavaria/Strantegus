

import pygame


class Tile(pygame.sprite.Sprite):
    image = None
    rect = None
    x = 0
    y = 0

    def __init__(self, world):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        world.tiles.add(self)
