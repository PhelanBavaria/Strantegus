

import pygame
from common.objects import Object


class Resource(Object):
    def __init__(self, world, amount):
        self.surface_size = (amount, amount)
        Object.__init__(self, world)
        self.amount = amount
        self.name = 'noname'
        world.resources.add(self)

    def update(self):
        self.surface_size = (self.amount, self.amount)
        center = self.rect.center
        self.rect.size = self.surface_size
        self.image = pygame.transform.scale(self.image, self.surface_size)
        self.rect.center = center
        if self.amount == 0:
            self.kill()
        elif self.amount < 0:
            raise ValueError('Amount of resource '+str(self)+' below 0')
