

import pygame


class BaseResource(pygame.sprite.Sprite):
    __slots__ = [
        'world',
        'amount',
        'name']
    color = (0, 200, 0)

    def __init__(self, world, amount):
        pygame.sprite.Sprite.__init__(self)
        surface_size = (amount, amount)
        self.world = world
        self.amount = amount
        self.name = 'noname'
        self.image = pygame.Surface(surface_size)
        self.image.convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        world.resources.add(self)

    def update(self):
        surface_size = (self.amount, self.amount)
        center = self.rect.center
        self.rect.size = surface_size
        self.image = pygame.transform.scale(self.image, surface_size)
        self.rect.center = center
        if self.amount == 0:
            self.kill()
        elif self.amount < 0:
            raise ValueError('Amount of resource '+str(self)+' below 0')
