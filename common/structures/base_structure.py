

import pygame


class Structure:
    def __init__(self, tile=None, size=5, auto_increment=0):
        self.tile = tile
        self.tiles = pygame.sprite.Group()
        self.size = size
        self.auto_increment = auto_increment

    def update(self):
        if self.auto_increment:
            self.size += self.auto_increment
            self.increase()

    def increase(self):
        tile = self.tile()
        self.tiles.add(tile)

    def colliding(self, sprites):
        for sprite in sprites:
            yield pygame.sprite.spritecollide(sprite, self.tiles)
