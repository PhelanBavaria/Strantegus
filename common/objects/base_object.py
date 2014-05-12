

import pygame


class Object(pygame.sprite.Sprite):
    _objects = pygame.sprite.Group()
    color = (0, 200, 0)
    surface_size = (8, 8)
    def __init__(self, world):
        pygame.sprite.Sprite.__init__(self)
        self._objects.add(self)
        self.image = pygame.Surface(self.surface_size)
        self.image.convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.world = world
