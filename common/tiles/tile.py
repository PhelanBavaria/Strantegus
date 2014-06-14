

import pygame
from config import TILE_SIZE
from util.load import load_image


class BaseTile(pygame.sprite.Sprite):
    __slots__ = ['world']
    x = 0
    y = 0

    def __init__(self, world, image, level='surface'):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image+'.bmp')
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.world = world
        world.tiles.add(self)
        world.levels[level][0].add(self)

    def mine(self):
        return
