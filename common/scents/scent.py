

import pygame
import config


class Scent(pygame.sprite.Sprite):
    __slots__ = [
        'ant',
        'amount',
        'turn']
    color = (120, 120, 120)

    def __init__(self, ant, amount):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((amount, amount))
        self.image.convert()
        self.image.set_alpha(min(255, amount))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.ant = ant
        self.amount = amount
        self.turn = ant.world.current_tick
        self.rect.center = ant.rect.center
