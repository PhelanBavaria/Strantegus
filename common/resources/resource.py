

import pygame


class BaseResource(pygame.sprite.Sprite):
    __slots__ = [
        'world',
        'amount',
        'name']
    color = (0, 200, 0)

    def __init__(self, world, amount, level='surface'):
        pygame.sprite.Sprite.__init__(self)
        surface_size = (amount/100, amount/100)
        self.world = world
        self.amount = amount
        self.name = 'noname'
        self.image = pygame.Surface(surface_size)
        self.image.convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        world.levels[level]['foreground'].add(self)
