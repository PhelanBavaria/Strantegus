

import pygame


class Resource(pygame.sprite.Sprite):
    color = (0, 200, 0)
    def __init__(self, world, amount):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.surface_size = (amount, amount)
        self.amount = amount
        self.name = 'noname'
        self.image = pygame.Surface(self.surface_size)
        self.image.convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
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
